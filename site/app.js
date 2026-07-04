(function () {
  const state = {
    feed: null,
    rows: [],
  };

  const providerFilter = document.querySelector("#provider-filter");
  const statusFilter = document.querySelector("#status-filter");
  const sortSelect = document.querySelector("#sort-select");
  const body = document.querySelector("#models-body");
  const summary = document.querySelector("#summary");

  function fmtPrice(value) {
    return value === null || value === undefined ? "-" : `$${Number(value).toLocaleString(undefined, { maximumFractionDigits: 6 })}`;
  }

  function fmtTokens(value) {
    return value === null || value === undefined ? "-" : Number(value).toLocaleString();
  }

  function uniq(values) {
    return Array.from(new Set(values)).sort((a, b) => a.localeCompare(b));
  }

  function priceValue(row, kind) {
    const value = row.pricing[kind];
    return value === null || value === undefined ? Number.POSITIVE_INFINITY : value;
  }

  function sortRows(rows) {
    const mode = sortSelect.value;
    const copy = rows.slice();
    if (mode === "input_asc") {
      copy.sort((a, b) => priceValue(a, "input_per_mtok") - priceValue(b, "input_per_mtok"));
    } else if (mode === "input_desc") {
      copy.sort((a, b) => priceValue(b, "input_per_mtok") - priceValue(a, "input_per_mtok"));
    } else if (mode === "output_asc") {
      copy.sort((a, b) => priceValue(a, "output_per_mtok") - priceValue(b, "output_per_mtok"));
    } else if (mode === "output_desc") {
      copy.sort((a, b) => priceValue(b, "output_per_mtok") - priceValue(a, "output_per_mtok"));
    } else {
      copy.sort((a, b) => `${a.provider}:${a.model_id}`.localeCompare(`${b.provider}:${b.model_id}`));
    }
    return copy;
  }

  function render() {
    const provider = providerFilter.value;
    const status = statusFilter.value;
    const filtered = state.rows.filter((row) => {
      return (!provider || row.provider === provider) && (!status || row.status === status);
    });
    const rows = sortRows(filtered);

    body.textContent = "";
    const fragment = document.createDocumentFragment();
    for (const row of rows) {
      const tr = document.createElement("tr");
      const sources = row.sources
        .map((source, index) => `<a href="${source.url}" target="_blank" rel="noreferrer">source ${index + 1}</a>`)
        .join("");
      tr.innerHTML = `
        <td>${row.provider}</td>
        <td><span class="mono">${row.model_id}</span><br>${row.display_name}</td>
        <td><span class="badge ${row.status}">${row.status}</span></td>
        <td>${fmtPrice(row.pricing.input_per_mtok)}</td>
        <td>${fmtPrice(row.pricing.cached_input_per_mtok)}</td>
        <td>${fmtPrice(row.pricing.output_per_mtok)}</td>
        <td>${fmtTokens(row.context_window_tokens)}</td>
        <td>${fmtTokens(row.max_output_tokens)}</td>
        <td>${row.modalities.input.join("+")} -> ${row.modalities.output.join("+")}</td>
        <td><div class="sources">${sources}</div></td>
      `;
      fragment.appendChild(tr);
    }
    body.appendChild(fragment);
    summary.textContent = `${rows.length} of ${state.rows.length} models`;
  }

  function fillFilters() {
    for (const provider of uniq(state.rows.map((row) => row.provider))) {
      providerFilter.append(new Option(provider, provider));
    }
    for (const status of uniq(state.rows.map((row) => row.status))) {
      statusFilter.append(new Option(status, status));
    }
  }

  async function loadFeed() {
    if (window.location.protocol === "file:") {
      return loadInlineFeed();
    }

    try {
      const response = await fetch("feed.json", { cache: "no-store" });
      if (!response.ok) {
        throw new Error(`feed.json returned ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      return loadInlineFeed(error);
    }
  }

  function loadInlineFeed(error) {
    const fallback = document.querySelector("#modelwire-feed");
    if (!fallback || !fallback.textContent.trim()) {
      throw error || new Error("No embedded feed fallback found");
    }
    return JSON.parse(fallback.textContent);
  }

  async function init() {
    try {
      state.feed = await loadFeed();
      state.rows = state.feed.models || [];
      fillFilters();
      providerFilter.addEventListener("change", render);
      statusFilter.addEventListener("change", render);
      sortSelect.addEventListener("change", render);
      render();
    } catch (error) {
      summary.textContent = "Unable to load feed";
      body.innerHTML = `<tr><td colspan="10">${error.message}</td></tr>`;
    }
  }

  init();
})();
