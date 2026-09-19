/* 3D family tree for the Mahjong Compendium landing page.
   A cone-tree: each node's children sit on a circle below it, with each child
   given an angular span proportional to how many leaves hang under it, so wide
   branches do not collide. Plain Three.js r128 globals, no module loader, and
   its own minimal orbit control so the page pulls in only one script. */
(function () {
  "use strict";
  var canvas = document.getElementById("tree");
  var tip = document.getElementById("tip");
  if (!canvas || !window.THREE) return;

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  fetch("assets/tree.json").then(function (r) { return r.json(); }).then(build).catch(function () {
    canvas.parentNode.insertAdjacentHTML("beforeend",
      '<p class="hint">The tree could not load. <a href="variants/">Browse the variants</a> instead.</p>');
  });

  function build(nodes) {
    var byId = {}, roots = [];
    nodes.forEach(function (n) { byId[n.slug] = n; n.kids = []; });
    nodes.forEach(function (n) { n.parent ? byId[n.parent].kids.push(n) : roots.push(n); });

    // Radial tree: depth sets the ring radius, so every generation gets MORE
    // room than the one above it rather than less, and a node's angular wedge is
    // proportional to the leaves beneath it so siblings never collide.
    function weigh(n) {
      n.leaves = n.kids.length ? n.kids.reduce(function (s, k) { return s + weigh(k); }, 0) : 1;
      return n.leaves;
    }
    roots.forEach(weigh);

    // Rings widen with depth and each generation drops a full step, so the
    // tree reads as a descending funnel rather than a flat disk.
    var RING = 15, DROP = 21, R0 = 22;
    function ring(d) { return R0 + d * RING; }

    // A wedge purely proportional to leaf count squeezes a parent's small
    // branches into slivers, and at a given ring that means overlapping nodes.
    // So every child is guaranteed MIN_ARC of arc length, taken proportionally
    // from the siblings that have room to spare.
    var MIN_ARC = 13;
    function shares(span, kids, radius) {
      var floor = Math.min(span / kids.length, MIN_ARC / radius);
      var sum = kids.reduce(function (s, k) { return s + k.leaves; }, 0);
      var out = kids.map(function (k) { return (span * k.leaves) / sum; });
      var short = 0, slack = 0;
      out.forEach(function (v) { v < floor ? (short += floor - v) : (slack += v - floor); });
      if (short > 0 && slack > short) {
        var f = (slack - short) / slack;
        out = out.map(function (v) { return v < floor ? floor : floor + (v - floor) * f; });
      } else if (short > 0) {
        out = out.map(function () { return span / kids.length; });
      }
      return out;
    }

    var cursor = 0;
    shares(Math.PI * 2, roots, ring(0)).forEach(function (span, i) {
      seat(roots[i], cursor, cursor + span);
      cursor += span;
    });

    function seat(n, a0, a1) {
      var mid = (a0 + a1) / 2;
      n.x = Math.cos(mid) * ring(n.depth);
      n.z = Math.sin(mid) * ring(n.depth);
      n.y = -n.depth * DROP;
      if (!n.kids.length) return;
      var acc = a0;
      shares(a1 - a0, n.kids, ring(n.depth + 1)).forEach(function (span, i) {
        seat(n.kids[i], acc, acc + span);
        acc += span;
      });
    }

    var scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x0b1f18, 0.0032);
    var camera = new THREE.PerspectiveCamera(52, 1, 0.1, 2000);
    var renderer;
    try {
      renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    } catch (e) { return; }
    renderer.setClearColor(0x000000, 0);

    // edges
    var epos = [];
    nodes.forEach(function (n) {
      if (!n.parent) return;
      var p = byId[n.parent];
      epos.push(p.x, p.y, p.z, n.x, n.y, n.z);
    });
    var eg = new THREE.BufferGeometry();
    eg.setAttribute("position", new THREE.Float32BufferAttribute(epos, 3));
    scene.add(new THREE.LineSegments(eg,
      new THREE.LineBasicMaterial({ color: 0x7d6a3d, transparent: true, opacity: 0.72 })));

    // nodes
    var geo = new THREE.SphereGeometry(1, 18, 14);
    var meshes = [];
    nodes.forEach(function (n) {
      var size = 2.4 + Math.max(0, 3 - n.depth) * 0.45;
      var m = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color: new THREE.Color(n.colour) }));
      m.position.set(n.x, n.y, n.z);
      m.scale.setScalar(size);
      m.userData = n;
      n.size = size;
      scene.add(m);
      // additive glow: where haloes overlap they brighten instead of stacking
      // into a flat grey cloud
      var halo = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({
        color: new THREE.Color(n.colour), transparent: true, opacity: 0.14,
        blending: THREE.AdditiveBlending, depthWrite: false, fog: false
      }));
      halo.position.copy(m.position);
      halo.scale.setScalar(size * 1.7);
      scene.add(halo);
      n.halo = halo;
      meshes.push(m);
    });

    // Labels live in the DOM, not as sprites: HTML text stays crisp at any zoom,
    // and a screen-space pass each frame can drop whichever ones would collide.
    // Shallow, heavily-branched nodes claim their space first, so the trunk is
    // always named and deeper labels appear as you zoom into the gaps.
    var layer = document.getElementById("labels");
    var labels = [];
    if (layer) {
      nodes.slice().sort(function (a, b) {
        return a.depth - b.depth || b.leaves - a.leaves;
      }).forEach(function (n) {
        var el = document.createElement("span");
        el.className = "lab";
        el.textContent = n.label;
        el.style.color = n.colour;
        layer.appendChild(el);
        labels.push({ n: n, el: el, w: 0, h: 0, on: false });
      });
    }

    // camera orbit state
    var lo = new THREE.Vector3(Infinity, Infinity, Infinity);
    var hi = new THREE.Vector3(-Infinity, -Infinity, -Infinity);
    nodes.forEach(function (n) {
      lo.min(new THREE.Vector3(n.x, n.y, n.z));
      hi.max(new THREE.Vector3(n.x, n.y, n.z));
    });
    var target = lo.clone().add(hi).multiplyScalar(0.5);
    // radius of the sphere that encloses every node, measured from the centre
    // the camera looks at, so the fit below never crops a branch
    var reach = 1;
    nodes.forEach(function (n) {
      reach = Math.max(reach, target.distanceTo(new THREE.Vector3(n.x, n.y, n.z)));
    });
    var yaw = 0.55, pitch = 0.58, fit = reach * 2.4, zoom = 1, dist = fit;
    var proj = new THREE.Vector3(), rgt = new THREE.Vector3(), upv = new THREE.Vector3();
    var drag = null, moved = false;

    function apply() {
      dist = fit * zoom;
      camera.position.set(
        target.x + dist * Math.cos(pitch) * Math.sin(yaw),
        target.y + dist * Math.sin(pitch),
        target.z + dist * Math.cos(pitch) * Math.cos(yaw)
      );
      camera.lookAt(target);
    }

    // Fit the tree to the viewport by measuring where it actually lands on
    // screen, not by enclosing it in a sphere: the layout is a wide flat disk
    // seen at an angle, so a sphere fit would leave most of the frame empty.
    // Each pass recentres the look-at point on the projected bounds, then
    // corrects the distance; four passes are plenty to settle.
    function frame() {
      for (var pass = 0; pass < 4; pass++) {
        apply();
        camera.updateMatrixWorld();
        var x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
        for (var i = 0; i < nodes.length; i++) {
          proj.set(nodes[i].x, nodes[i].y, nodes[i].z).project(camera);
          if (proj.x < x0) x0 = proj.x;
          if (proj.x > x1) x1 = proj.x;
          if (proj.y < y0) y0 = proj.y;
          if (proj.y > y1) y1 = proj.y;
        }
        camera.matrixWorld.extractBasis(rgt, upv, new THREE.Vector3());
        var half = dist * Math.tan((camera.fov * Math.PI) / 360);
        target.addScaledVector(rgt, ((x0 + x1) / 2) * half * camera.aspect);
        target.addScaledVector(upv, ((y0 + y1) / 2) * half);
        fit *= Math.max((x1 - x0) / 2 / 0.86, (y1 - y0) / 2 / 0.8);
      }
      apply();
    }

    function resize() {
      var w = canvas.clientWidth, h = canvas.clientHeight;
      if (!w || !h) return;
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      frame();
    }
    window.addEventListener("resize", resize);
    resize();

    canvas.addEventListener("pointerdown", function (e) {
      drag = { x: e.clientX, y: e.clientY }; moved = false;
      canvas.setPointerCapture(e.pointerId);
    });
    canvas.addEventListener("pointermove", function (e) {
      if (drag) {
        var dx = e.clientX - drag.x, dy = e.clientY - drag.y;
        if (Math.abs(dx) + Math.abs(dy) > 3) moved = true;
        yaw -= dx * 0.006;
        pitch = Math.max(-0.35, Math.min(1.25, pitch + dy * 0.005));
        drag = { x: e.clientX, y: e.clientY };
        apply();
      } else hover(e);
    });
    canvas.addEventListener("pointerup", function (e) {
      drag = null;
      canvas.releasePointerCapture(e.pointerId);
      if (!moved) click(e);
    });
    canvas.addEventListener("pointerleave", function () { drag = null; hide(); });
    canvas.addEventListener("wheel", function (e) {
      e.preventDefault();
      zoom = Math.max(0.3, Math.min(2.6, zoom * (1 + e.deltaY * 0.0012)));
      apply();
    }, { passive: false });

    var ray = new THREE.Raycaster(), ndc = new THREE.Vector2(), hot = null;

    function pick(e) {
      var r = canvas.getBoundingClientRect();
      ndc.x = ((e.clientX - r.left) / r.width) * 2 - 1;
      ndc.y = -((e.clientY - r.top) / r.height) * 2 + 1;
      ray.setFromCamera(ndc, camera);
      var hit = ray.intersectObjects(meshes, false);
      return hit.length ? hit[0].object : null;
    }
    function hover(e) {
      var m = pick(e);
      if (!m) { hide(); return; }
      hot = m.userData;
      var r = canvas.getBoundingClientRect();
      tip.style.left = (e.clientX - r.left) + "px";
      tip.style.top = (e.clientY - r.top) + "px";
      tip.style.borderLeftColor = hot.colour;
      tip.innerHTML = "<b></b><span></span>";
      tip.firstChild.textContent = hot.label;
      tip.lastChild.textContent =
        (hot.detail ? hot.detail + " · " : "") + (hot.evidence || "");
      tip.hidden = false;
      canvas.style.cursor = "pointer";
    }
    function hide() { tip.hidden = true; hot = null; canvas.style.cursor = ""; }
    function click(e) {
      var m = pick(e);
      if (m) location.href = "variants/" + m.userData.slug + "/";
    }

    var taken = [];

    function place() {
      var w = canvas.clientWidth, h = canvas.clientHeight;
      if (!w || !h) return;
      taken.length = 0;
      for (var i = 0; i < labels.length; i++) {
        var L = labels[i], n = L.n;
        proj.set(n.x, n.y, n.z).project(camera);
        var show = proj.z < 1 && Math.abs(proj.x) < 1 && Math.abs(proj.y) < 1;
        var x = 0, y = 0;
        if (show) {
          if (!L.w) { L.w = L.el.offsetWidth; L.h = L.el.offsetHeight; }
          x = (proj.x * 0.5 + 0.5) * w;
          y = (-proj.y * 0.5 + 0.5) * h - 13;
          var box = [x - L.w / 2 - 4, y - L.h - 3, x + L.w / 2 + 4, y + 3];
          if (box[0] < 0 || box[2] > w || box[1] < 0 || box[3] > h) show = false;
          for (var j = 0; show && j < taken.length; j++) {
            var t = taken[j];
            if (box[0] < t[2] && box[2] > t[0] && box[1] < t[3] && box[3] > t[1]) show = false;
          }
          if (show) taken.push(box);
        }
        if (show) {
          L.el.style.transform =
            "translate(" + Math.round(x) + "px," + Math.round(y) + "px) translate(-50%,-100%)";
        }
        if (show !== L.on) { L.el.classList.toggle("on", show); L.on = show; }
      }
    }

    // Nodes are sized in screen space rather than world space: the generations
    // nearest the camera would otherwise swell into featureless discs.
    function sizes() {
      for (var i = 0; i < meshes.length; i++) {
        var m = meshes[i], n = m.userData;
        var k = camera.position.distanceTo(m.position) / fit;
        m.scale.setScalar(n.size * k);
        n.halo.scale.setScalar(n.size * 1.7 * k);
      }
    }

    apply();
    var spin = !reduced;
    canvas.addEventListener("pointerdown", function () { spin = false; });
    (function loop() {
      requestAnimationFrame(loop);
      if (spin) { yaw += 0.0012; apply(); }
      sizes();
      renderer.render(scene, camera);
      place();
    })();
  }
})();
