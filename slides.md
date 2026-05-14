---
theme: seriph
background: https://cover.sli.dev
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Vibe Coding 实践分享
drawings:
  persist: false
transition: slide-left
title: Vibe Coding 实践分享
---

# Vibe Coding 实践分享

<div class="pt-12">
  <p class="text-xl"><b>日期：</b> 5月15日</p>
</div>

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    开始 <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: center
class: text-center
---

# 免责声明

本分享只代表本人截止 2026 年 5 月 15 日的观点。

内容会随着工具、模型和实践经验变化而更新。

---
layout: default
---

# 分享框架

<div class="grid grid-cols-2 gap-8 pt-8">
  <div>
    <h2>第一部分：Vibe Coding 是什么</h2>
    <ul>
      <li>模型</li>
      <li>提示词</li>
      <li>上下文</li>
    </ul>
  </div>
  <div>
    <h2>第二部分：实践内容</h2>
    <ul>
      <li>任务拆解</li>
      <li>上下文管理</li>
      <li>验证与迭代</li>
    </ul>
  </div>
</div>

---
layout: section
---

# 第一部分

Vibe Coding 是什么

---
layout: default
---

# 1. 模型

<div class="model-page">
  <p class="model-lead">模型重要，但真正决定质量的是设计。</p>

  <ul class="model-points">
    <li>模型会影响效率，但不是代码质量的决定性因素</li>
    <li>好代码首先来自清晰设计，而不是更强模型</li>
    <li>“一句话生成一堆代码”必然引入大量随机性</li>
    <li>想让结果可控，就要给 AI 更明确的设计输入</li>
  </ul>
</div>

<!--
讲模型时，我想先回应一个很常见的担心：如果模型没那么强，生成出来的代码质量是不是就不可靠？或者说，它到底能不能正确地把功能实现出来？这个担心是合理的，因为我们直觉上会把 AI 编程的效果直接归因到模型能力上，好像模型越强，代码就越好。但我的看法稍微不一样：在目前这个阶段，模型当然会影响效率和体验，但它不是最终代码质量的决定性因素。

原因在于，我们平时评价一段代码好不好，看的并不只是它能不能跑起来。功能正确只是底线，真正决定软件质量的，是它后面好不好维护、好不好扩展，有没有重复逻辑，数据来源是不是单一，修改一个地方会不会影响一大片。这些问题本质上都不是“某一行代码写得漂不漂亮”的问题，而是设计问题。

如果设计已经足够清楚，比如模块边界是什么，每个函数负责什么，输入输出是什么，状态应该放在哪里，和现有代码怎么交互，这些都已经确定了，那么大多数模型其实都可以把实现写到一个可接受的程度。哪怕不是最顶级的模型，只要你给它的信息足够明确，它通常也能生成正确的代码。反过来，如果设计本身是模糊的，换一个更强的模型，也只是让它用更流畅的方式替你做猜测。

这里面有一个很关键的信息量问题。Vibe Coding 很多时候是我们用一句很短的话，让 AI 生成一大段代码。但输入的信息量很少，输出的代码信息量却很大，中间缺失的部分不可能凭空消失，只能由模型自己补全。模型补全出来的东西可能可以运行，但不一定符合我们的预期，也不一定符合项目长期维护的要求。所以所谓“AI 写得不对”，很多时候不是它不会写，而是我们没有把判断标准和设计约束给清楚。

所以我觉得，想让 AI 生成的代码更稳定、更接近我们想要的结果，核心方法不是只追逐更强的模型，而是减少它需要自由发挥的空间。我们对最终结果要求越明确，给它的信息越充分，它生成的东西就越可控。比如你能告诉它要写哪些函数，每个函数接收什么、返回什么，错误怎么处理，数据从哪里来，哪些代码不能改，哪些行为必须保持兼容，它就更容易写出你愿意接受的代码。

换句话说，在 Vibe Coding 里，模型更像是实现能力，而不是设计能力的替代品。它可以帮我们把已经想清楚的方案快速落地，但它不能替我们决定什么样的软件结构是长期可维护的。人的核心价值并没有消失，只是从“逐行写代码”转移到了“定义问题、设计结构、约束结果”上。
-->

---
layout: default
---

# 2. 提示词

- 把想法说清楚
- 给出目标、背景和约束
- 让输出更可控

---
layout: default
---

# 3. 上下文

- 让 AI 看见正确的信息
- 控制文件、历史和资料范围
- 减少误解和幻觉

---
layout: section
---

# 第二部分

实践内容

---
layout: default
---

# 1. 任务拆解

- 把目标拆成可执行的小任务
- 每一步都有明确输入和输出
- 避免一次交给 AI 太大范围

---
layout: default
---

# 2. 上下文管理

- 给 AI 看正确的文件和资料
- 保持问题背景清楚
- 及时清理无关信息

---
layout: default
---

# 3. 验证与迭代

- Review 生成结果
- 跑测试或做最小验证
- 根据反馈继续调整

---
layout: center
class: text-center
---

# Q&A

<style>
.model-page {
  margin-top: 2rem;
  max-width: 46rem;
}

.model-lead {
  margin: 0 0 2.4rem;
  color: #334155;
  font-size: 1.55rem;
  line-height: 1.55;
}

.model-points {
  margin: 0;
  padding-left: 1.35rem;
}

.model-points li {
  margin: 0 0 1.15rem;
  padding-left: 0.25rem;
  color: #0f172a;
  font-size: 1.18rem;
  line-height: 1.65;
}

.model-points li::marker {
  color: #64748b;
  font-size: 0.9em;
}
</style>
