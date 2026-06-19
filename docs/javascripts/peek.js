/* Hover "peek" popover for cross-reference links (a.xref[data-peek]).
   Uses event delegation on document so it survives Material's instant navigation. */
(function () {
  let pop = null;

  function popover() {
    if (!pop) {
      pop = document.createElement("div");
      pop.className = "api-peek";
      pop.setAttribute("role", "tooltip");
      pop.style.display = "none";
      document.body.appendChild(pop);
    }
    return pop;
  }

  function show(link) {
    const text = link.getAttribute("data-peek");
    if (!text) return;
    const el = popover();
    el.textContent = text;
    el.style.display = "block";

    const r = link.getBoundingClientRect();
    el.style.top = window.scrollY + r.bottom + 6 + "px";
    el.style.left = window.scrollX + r.left + "px";

    // Nudge back inside the viewport if it overflows on the right.
    const pr = el.getBoundingClientRect();
    if (pr.right > window.innerWidth - 8) {
      el.style.left =
        Math.max(8, window.scrollX + window.innerWidth - pr.width - 8) + "px";
    }
  }

  function hide() {
    if (pop) pop.style.display = "none";
  }

  document.addEventListener("mouseover", function (e) {
    const link = e.target.closest && e.target.closest("a.xref");
    if (link) show(link);
  });
  document.addEventListener("mouseout", function (e) {
    const link = e.target.closest && e.target.closest("a.xref");
    if (link) hide();
  });
  document.addEventListener("click", hide, true);
})();

/* Briefly highlight the definition you jump to, so it's easy to spot.
   Triggered on the click itself (capture phase) so it works regardless of
   Material's instant navigation, which doesn't fire load/hashchange. */
(function () {
  function flashEl(el) {
    if (!el) return false;
    const block = el.closest("li, p, tr") || el;
    block.classList.remove("api-target-flash");
    void block.offsetWidth; // force reflow so the animation restarts every time
    block.classList.add("api-target-flash");
    return true;
  }
  function flashId(id, tries) {
    if (!id) return;
    // Same-page: the element is already here. Cross-page (instant nav): retry
    // until the swapped-in content contains it.
    if (flashEl(document.getElementById(id))) return;
    if (tries > 0) setTimeout(function () { flashId(id, tries - 1); }, 120);
  }
  function idFromHref(href) {
    const i = href.indexOf("#");
    return i >= 0 ? decodeURIComponent(href.slice(i + 1)) : "";
  }
  document.addEventListener(
    "click",
    function (e) {
      const link = e.target.closest && e.target.closest("a.xref");
      if (link) flashId(idFromHref(link.getAttribute("href") || ""), 12);
    },
    true
  );
  // Also cover deep links opened directly and back/forward navigation.
  function flashFromHash() {
    flashId(location.hash ? decodeURIComponent(location.hash.slice(1)) : "", 6);
  }
  window.addEventListener("hashchange", flashFromHash);
  window.addEventListener("load", flashFromHash);
  document.addEventListener("animationend", function (e) {
    if (e.target.classList && e.target.classList.contains("api-target-flash")) {
      e.target.classList.remove("api-target-flash");
    }
  });
})();
