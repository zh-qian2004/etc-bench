(function () {
  "use strict";

  const data = window.ETC_DEMO_DATA;
  if (!data) {
    document.body.innerHTML = '<p style="padding:2rem;font-family:sans-serif">Demo data is missing. Run <code>demo/build_data.py</code>.</p>';
    return;
  }

  const copy = {
    en: {
      navBenchmark: "Benchmark", navResults: "Results", navExplorer: "Output explorer",
      heroEyebrow: "Interactive benchmark and system outputs",
      heroTitle: "Explore canonicalization of speech-equivalent transcript variants.",
      heroLead: "Browse ETC-Bench samples, compare outputs from TACS-based agents and compact model canonicalizers, and inspect how exact match and semantic preservation determine SENA.",
      exploreOutputs: "Explore outputs", compareSystems: "Compare systems", heroExample: "Canonicalization example",
      benchmarkEyebrow: "The benchmark", benchmarkTitle: "A multilingual view of transcript ambiguity",
      benchmarkLead: "Each item is a pair of valid written representations of the same spoken utterance. Filters below update the distribution and open a matching example in the output explorer.",
      taxonomyEyebrow: "Five-category taxonomy", taxonomyTitle: "From enumerable forms to language-specific ambiguity",
      taxonomyLead: "Numeric expressions and symbols are language-agnostic at the phenomenon level. Abbreviations, orthographic variants, and homophonic substitutions depend on each language.",
      resultsEyebrow: "Evaluation results", resultsTitle: "TACS agents and compact model canonicalizers",
      resultsLead: "TACS values are three-run results reported in the paper. Released compact models use one deterministic full-benchmark run. Select a system to inspect its language and category profile.",
      byLanguage: "By language", byCategory: "By category",
      explorerEyebrow: "Pair-level inspection", explorerTitle: "Benchmark sample and canonical outputs",
      explorerLead: "Filter the complete release, then compare how each system transforms the two transcripts. TACS outputs shown here come from one representative run rather than an average of strings across runs.",
      filterLanguage: "Language", filterCategory: "Category", filterPhenomenon: "Phenomenon", filterSearch: "Search text or ID",
      filterOutcome: "Selected-system outcome", clearFilters: "Clear", randomSample: "Random sample",
      canonicalOutputs: "Canonical outputs", exactCondition: "Exact-match condition", semanticCondition: "Semantic-preservation condition", senaCredit: "SENA credit",
      metricDetails: "Show metric values", metricTLabel: "source-pair similarity", metricFLabel: "lower input–output similarity", metricDeltaLabel: "similarity tolerance",
      footerText: "Evaluation-side Transcript Canonicalization",
      items: "pairs", languages: "languages", phenomena: "distinct phenomena", categories: "categories",
      agnostic: "Language-agnostic", specific: "Language-specific", all: "All", credit: "Receives credit", noCredit: "No credit", exactFail: "Exact-match failure", semanticFail: "Semantic-preservation failure",
      matches: "matching pairs", noMatches: "No benchmark pairs match these filters.",
      exactPass: "The two canonical outputs are identical.", exactFailText: "The two canonical outputs remain different.",
      semanticPass: "The similarity decrease stays within δ = 0.10.", semanticFailText: "The similarity decrease exceeds δ = 0.10.",
      outputRun: "Representative output run", reported: "Reported SENA", chooseSystem: "Select a system",
      tacsAgent: "TACS agent", modelCanonicalizer: "Model canonicalizer", tacsScoreNote: "Mean of three runs reported in the paper", modelScoreNote: "Single deterministic full-release evaluation",
    },
    zh: {
      navBenchmark: "基准", navResults: "结果", navExplorer: "输出浏览器",
      heroEyebrow: "交互式基准与系统输出",
      heroTitle: "观察不同转写形式映射到同一规范形式。",
      heroLead: "浏览语音等价的转写文本对，检查五个 canonicalization 系统，并查看每个样本获得或未获得 SENA 分数的具体原因。",
      exploreOutputs: "浏览输出", compareSystems: "比较系统", heroExample: "Canonicalization 示例",
      benchmarkEyebrow: "基准数据", benchmarkTitle: "多语种转写歧义的结构化视图",
      benchmarkLead: "每个样本包含同一段语音的两种有效书面表达。下面的筛选项会更新数据分布，并在输出浏览器中打开相应样本。",
      taxonomyEyebrow: "五类现象体系", taxonomyTitle: "从封闭可枚举形式到语种特定歧义",
      taxonomyLead: "数字表达和符号标记在现象层面与语种无关；缩写、正字法变体和同音替换依赖具体语种。",
      resultsEyebrow: "测评结果", resultsTitle: "TACS agent 与轻量模型 canonicalizer",
      resultsLead: "TACS 数值是论文报告的三轮均值；开源小模型使用一次确定性的完整基准测评。选择系统可查看分语种和分类别表现。",
      byLanguage: "按语种", byCategory: "按类别",
      explorerEyebrow: "逐样本检查", explorerTitle: "基准样本与规范化输出",
      explorerLead: "筛选完整发布集，然后比较各系统如何处理文本对的两侧。这里展示的 TACS 文本输出来自一轮代表性运行，而不是对多轮文本求平均。",
      filterLanguage: "语种", filterCategory: "类别", filterPhenomenon: "现象", filterSearch: "搜索文本或 ID",
      filterOutcome: "所选系统结果", clearFilters: "清除", randomSample: "随机样本",
      canonicalOutputs: "规范化输出", exactCondition: "Exact-match 条件", semanticCondition: "Semantic-preservation 条件", senaCredit: "SENA 得分",
      metricDetails: "查看指标数值", metricTLabel: "原始文本对相似度", metricFLabel: "较低的输入—输出相似度", metricDeltaLabel: "相似度容差",
      footerText: "Evaluation-side Transcript Canonicalization",
      items: "个文本对", languages: "个语种", phenomena: "个不同现象", categories: "个类别",
      agnostic: "Language-agnostic", specific: "Language-specific", all: "全部", credit: "获得分数", noCredit: "未获得分数", exactFail: "Exact-match 未通过", semanticFail: "Semantic-preservation 未通过",
      matches: "个匹配样本", noMatches: "没有样本符合当前筛选条件。",
      exactPass: "两个 canonical outputs 完全相同。", exactFailText: "两个 canonical outputs 仍不相同。",
      semanticPass: "相似度下降未超过 δ = 0.10。", semanticFailText: "相似度下降超过 δ = 0.10。",
      outputRun: "代表性输出轮次", reported: "报告的 SENA", chooseSystem: "选择系统",
      tacsAgent: "TACS agent", modelCanonicalizer: "模型 canonicalizer", tacsScoreNote: "论文报告的三轮均值", modelScoreNote: "单次确定性全量测评",
    },
  };

  const params = new URLSearchParams(location.search);
  const state = {
    uiLanguage: params.get("lang") === "zh" ? "zh" : "en",
    resultSystem: params.get("result") || "tacs-qwen",
    outputSystem: params.get("system") || "tacs-qwen",
    dimension: "languages",
    activeId: params.get("item") || data.items[0]?.id,
    filters: { language: "all", category: "all", phenomenon: "all", outcome: "all", search: "" },
  };

  const $ = (id) => document.getElementById(id);
  const tr = (key) => copy[state.uiLanguage][key] || key;
  const systemById = (id) => data.systems.find((system) => system.id === id) || data.systems[0];
  const systemKind = (system) => tr(system.kind === "TACS agent" ? "tacsAgent" : "modelCanonicalizer");
  const scoreNote = (system) => tr(system.kind === "TACS agent" ? "tacsScoreNote" : "modelScoreNote");
  const titleCase = (value) => value.replaceAll("_", " ").replace(/\b\w/g, (letter) => letter.toUpperCase());
  const option = (value, label) => {
    const node = document.createElement("option");
    node.value = value;
    node.textContent = label;
    return node;
  };

  function updateUrl() {
    const url = new URL(location.href);
    url.searchParams.set("lang", state.uiLanguage);
    url.searchParams.set("item", state.activeId);
    url.searchParams.set("system", state.outputSystem);
    url.searchParams.set("result", state.resultSystem);
    history.replaceState(null, "", url);
  }

  function renderCopy() {
    document.documentElement.lang = state.uiLanguage === "zh" ? "zh-CN" : "en";
    document.title = state.uiLanguage === "zh" ? "ETC-Bench · 交互演示" : "ETC-Bench · Interactive demo";
    document.querySelectorAll("[data-copy]").forEach((node) => { node.textContent = tr(node.dataset.copy); });
    document.querySelectorAll("[data-ui-language]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.uiLanguage === state.uiLanguage));
    });
  }

  function renderStats() {
    const entries = [
      [data.meta.items.toLocaleString(), tr("items")],
      [data.meta.languages, tr("languages")],
      [data.meta.phenomena, tr("phenomena")],
      [data.meta.categories, tr("categories")],
    ];
    $("statGrid").replaceChildren(...entries.map(([value, label]) => {
      const node = document.createElement("div");
      node.className = "stat";
      const strong = document.createElement("strong");
      strong.textContent = value;
      const span = document.createElement("span");
      span.textContent = label;
      node.append(strong, span);
      return node;
    }));
  }

  function renderCategoryMap() {
    const counts = Object.fromEntries(data.categoryOrder.map((category) => [category, 0]));
    data.items.forEach((item) => { counts[item.category] += 1; });
    $("categoryMap").replaceChildren(...data.categoryOrder.map((category, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "category-chip";
      const small = document.createElement("small");
      small.textContent = tr(index < 2 ? "agnostic" : "specific");
      const strong = document.createElement("strong");
      strong.textContent = data.categoryNames[category];
      const span = document.createElement("span");
      span.textContent = `${counts[category]} ${tr("items")}`;
      button.append(small, strong, span);
      button.addEventListener("click", () => {
        state.filters.category = category;
        $("categoryFilter").value = category;
        refreshPhenomena();
        refreshExplorer();
        $("explorer").scrollIntoView({ behavior: "smooth" });
      });
      return button;
    }));
  }

  function renderSystemCards() {
    $("systemCards").replaceChildren(...data.systems.map((system) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "system-card";
      button.setAttribute("aria-pressed", String(system.id === state.resultSystem));
      const kind = document.createElement("small");
      kind.textContent = systemKind(system);
      const name = document.createElement("strong");
      name.textContent = system.label;
      const score = document.createElement("span");
      score.className = "score";
      score.textContent = system.score.toFixed(1);
      const note = document.createElement("span");
      note.className = "protocol";
      note.textContent = scoreNote(system);
      button.append(kind, name, score, note);
      button.addEventListener("click", () => {
        state.resultSystem = system.id;
        renderSystemCards();
        renderResultDetail();
        updateUrl();
      });
      return button;
    }));
  }

  function renderResultDetail() {
    const system = systemById(state.resultSystem);
    $("detailKind").textContent = systemKind(system);
    $("detailTitle").textContent = system.label;
    $("detailNote").textContent = `${tr("reported")}: ${system.score.toFixed(1)}%. ${scoreNote(system)}.`;
    document.querySelectorAll("[data-dimension]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.dimension === state.dimension));
    });
    const values = system[state.dimension];
    const order = state.dimension === "languages" ? data.languageOrder : data.categoryOrder;
    const names = state.dimension === "languages" ? data.languageNames : data.categoryNames;
    const chart = $("barChart");
    chart.className = `bar-chart ${state.dimension}`;
    chart.replaceChildren(...order.map((key) => {
      const value = Number(values[key] || 0);
      const item = document.createElement("div");
      item.className = "bar-item";
      item.title = `${names[key]}: ${value.toFixed(1)}%`;
      const track = document.createElement("div");
      track.className = "bar-track";
      const fill = document.createElement("span");
      fill.className = "bar-fill";
      fill.style.height = `${value}%`;
      const valueNode = document.createElement("span");
      valueNode.className = "bar-value";
      valueNode.textContent = value.toFixed(1);
      track.append(fill, valueNode);
      const label = document.createElement("span");
      label.className = "bar-label";
      label.textContent = state.dimension === "languages" ? key : names[key];
      item.append(track, label);
      return item;
    }));
  }

  function populateFilters() {
    const language = $("languageFilter");
    language.replaceChildren(option("all", tr("all")), ...data.languageOrder.map((key) => option(key, `${data.languageNames[key]} (${key})`)));
    language.value = state.filters.language;
    const category = $("categoryFilter");
    category.replaceChildren(option("all", tr("all")), ...data.categoryOrder.map((key) => option(key, data.categoryNames[key])));
    category.value = state.filters.category;
    const outcome = $("outcomeFilter");
    outcome.replaceChildren(
      option("all", tr("all")), option("credit", tr("credit")), option("no-credit", tr("noCredit")),
      option("exact-fail", tr("exactFail")), option("semantic-fail", tr("semanticFail")),
    );
    outcome.value = state.filters.outcome;
    const system = $("outputSystemSelect");
    system.replaceChildren(...data.systems.map((entry) => option(entry.id, entry.label)));
    system.value = state.outputSystem;
    refreshPhenomena();
  }

  function refreshPhenomena() {
    const phenomena = [...new Set(data.items
      .filter((item) => state.filters.language === "all" || item.language === state.filters.language)
      .filter((item) => state.filters.category === "all" || item.category === state.filters.category)
      .map((item) => item.phenomenon))].sort();
    if (!phenomena.includes(state.filters.phenomenon)) state.filters.phenomenon = "all";
    $("phenomenonFilter").replaceChildren(option("all", tr("all")), ...phenomena.map((name) => option(name, titleCase(name))));
    $("phenomenonFilter").value = state.filters.phenomenon;
  }

  function filteredItems() {
    const query = state.filters.search.trim().toLocaleLowerCase();
    return data.items.filter((item) => {
      if (state.filters.language !== "all" && item.language !== state.filters.language) return false;
      if (state.filters.category !== "all" && item.category !== state.filters.category) return false;
      if (state.filters.phenomenon !== "all" && item.phenomenon !== state.filters.phenomenon) return false;
      if (query && !`${item.id} ${item.phenomenon} ${item.description} ${item.a} ${item.b}`.toLocaleLowerCase().includes(query)) return false;
      const output = item.outputs[state.outputSystem];
      if (state.filters.outcome === "credit" && !output.credited) return false;
      if (state.filters.outcome === "no-credit" && output.credited) return false;
      if (state.filters.outcome === "exact-fail" && output.exact) return false;
      if (state.filters.outcome === "semantic-fail" && output.semantic) return false;
      return true;
    });
  }

  function renderSampleList(items) {
    $("matchCount").textContent = `${items.length.toLocaleString()} ${tr("matches")}`;
    if (!items.length) {
      const empty = document.createElement("p");
      empty.className = "empty-list";
      empty.textContent = tr("noMatches");
      $("sampleList").replaceChildren(empty);
      return;
    }
    $("sampleList").replaceChildren(...items.map((item, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "sample-button";
      button.setAttribute("role", "option");
      button.setAttribute("aria-selected", String(item.id === state.activeId));
      const number = document.createElement("span");
      number.className = "sample-number";
      number.textContent = String(index + 1).padStart(3, "0");
      const text = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = `${item.language} · ${titleCase(item.phenomenon)}`;
      const small = document.createElement("small");
      small.textContent = item.a;
      text.append(strong, small);
      button.append(number, text);
      button.addEventListener("click", () => selectItem(item.id));
      return button;
    }));
  }

  function appendChangedText(node, text, comparison, className) {
    const left = Array.from(text);
    const right = Array.from(comparison);
    let prefix = 0;
    while (prefix < left.length && prefix < right.length && left[prefix] === right[prefix]) prefix += 1;
    let suffix = 0;
    while (suffix < left.length - prefix && suffix < right.length - prefix && left[left.length - 1 - suffix] === right[right.length - 1 - suffix]) suffix += 1;
    node.replaceChildren();
    node.append(document.createTextNode(left.slice(0, prefix).join("")));
    const middle = left.slice(prefix, left.length - suffix).join("");
    if (middle) {
      const mark = document.createElement("span");
      mark.className = className;
      mark.textContent = middle;
      node.append(mark);
    }
    node.append(document.createTextNode(suffix ? left.slice(left.length - suffix).join("") : ""));
  }

  function renderVerdict(node, pass, passText, failText) {
    node.classList.toggle("pass", pass);
    node.classList.toggle("fail", !pass);
    node.querySelector(".verdict-icon").textContent = pass ? "✓" : "×";
    node.querySelector("small").textContent = pass ? passText : failText;
  }

  function renderSample(item) {
    $("metaBadges").replaceChildren(...[
      [item.language, ""], [data.categoryNames[item.category], "category"], [titleCase(item.phenomenon), ""],
    ].map(([text, className]) => {
      const badge = document.createElement("span");
      badge.className = `badge ${className}`;
      badge.textContent = text;
      return badge;
    }));
    $("sampleId").textContent = `#${item.id}`;
    $("phenomenonTitle").textContent = titleCase(item.phenomenon);
    $("phenomenonDescription").textContent = item.description;
    appendChangedText($("sourceA"), item.a, item.b, "diff-remove");
    appendChangedText($("sourceB"), item.b, item.a, "diff-remove");

    const system = systemById(state.outputSystem);
    const output = item.outputs[state.outputSystem];
    $("outputSystemTitle").textContent = system.label;
    appendChangedText($("outputA"), output.a, item.a, "diff-add");
    appendChangedText($("outputB"), output.b, item.b, "diff-add");
    renderVerdict($("exactVerdict"), output.exact, tr("exactPass"), tr("exactFailText"));
    renderVerdict($("semanticVerdict"), output.semantic, tr("semanticPass"), tr("semanticFailText"));
    $("creditValue").textContent = output.credited ? "1" : "0";
    $("creditCard").classList.toggle("zero", !output.credited);
    $("metricT").textContent = output.t.toFixed(4);
    $("metricF").textContent = output.f.toFixed(4);
  }

  function selectItem(id) {
    state.activeId = id;
    const items = filteredItems();
    renderSampleList(items);
    const item = data.items.find((candidate) => candidate.id === id);
    if (item) renderSample(item);
    updateUrl();
  }

  function refreshExplorer() {
    const items = filteredItems();
    if (!items.some((item) => item.id === state.activeId)) state.activeId = items[0]?.id || data.items[0].id;
    renderSampleList(items);
    const item = data.items.find((candidate) => candidate.id === state.activeId);
    if (item) renderSample(item);
    updateUrl();
  }

  function bindEvents() {
    document.querySelectorAll("[data-ui-language]").forEach((button) => {
      button.addEventListener("click", () => {
        state.uiLanguage = button.dataset.uiLanguage;
        renderCopy(); renderStats(); renderCategoryMap(); populateFilters(); renderSystemCards(); renderResultDetail(); refreshExplorer();
      });
    });
    document.querySelectorAll("[data-dimension]").forEach((button) => {
      button.addEventListener("click", () => { state.dimension = button.dataset.dimension; renderResultDetail(); });
    });
    $("languageFilter").addEventListener("change", (event) => { state.filters.language = event.target.value; refreshPhenomena(); refreshExplorer(); });
    $("categoryFilter").addEventListener("change", (event) => { state.filters.category = event.target.value; refreshPhenomena(); refreshExplorer(); });
    $("phenomenonFilter").addEventListener("change", (event) => { state.filters.phenomenon = event.target.value; refreshExplorer(); });
    $("outcomeFilter").addEventListener("change", (event) => { state.filters.outcome = event.target.value; refreshExplorer(); });
    $("searchInput").addEventListener("input", (event) => { state.filters.search = event.target.value; refreshExplorer(); });
    $("outputSystemSelect").addEventListener("change", (event) => { state.outputSystem = event.target.value; refreshExplorer(); });
    $("clearFilters").addEventListener("click", () => {
      state.filters = { language: "all", category: "all", phenomenon: "all", outcome: "all", search: "" };
      $("searchInput").value = "";
      populateFilters(); refreshExplorer();
    });
    $("randomSample").addEventListener("click", () => {
      const items = filteredItems();
      if (items.length) selectItem(items[Math.floor(Math.random() * items.length)].id);
    });
  }

  function init() {
    if (!data.systems.some((system) => system.id === state.resultSystem)) state.resultSystem = data.systems[0].id;
    if (!data.systems.some((system) => system.id === state.outputSystem)) state.outputSystem = data.systems[0].id;
    if (!data.items.some((item) => item.id === state.activeId)) state.activeId = data.items[0].id;
    renderCopy(); renderStats(); renderCategoryMap(); renderSystemCards(); renderResultDetail(); populateFilters(); bindEvents(); refreshExplorer();
  }

  init();
})();
