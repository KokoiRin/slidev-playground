---
theme: seriph
background: https://cover.sli.dev
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## 锐评 Claude Code 与常用指令解析
  报告人: guoysh
drawings:
  persist: false
transition: slide-left
title: 锐评 Claude Code：从夯到拉
---

# 锐评 Claude Code：从「夯」到「拉」

兼谈 AI CLI 常用指令与最佳实践

<div class="pt-12">
  <p class="text-xl"><b>报告人：</b> guoysh</p>
  <p class="text-xl"><b>日期：</b> 5月15日</p>
</div>

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    开始锐评 <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# 锐评 🧐：为什么说它很「夯」？

初见惊艳，真正融入本地工作流的效率利器。

- 🚀 **理解力爆表** - 底座模型智商在线，能快速 Get 到项目意图，顺藤摸瓜找代码。
- 🛠️ **全自动驾驶** - 自己翻文件、自己搜代码、自己跑命令看报错。
- 💻 **无需切换上下文** - 留在终端里解决一切，不用在 IDE 和网页之间反复横跳。
- 🧩 **生态兼容** - 配合 MCP (Model Context Protocol) 等工具链简直是神仙打架。

---
layout: default
---

# 锐评 📉：又是怎么变「拉」的？

深度使用后，那些让人血压升高的瞬间。

- 💸 **Token 刺客** - 遇到复杂项目，动不动就把大量没用的文件塞进上下文，账单原地爆炸。
- 🔄 **死循环大师** - 典型的“又菜又爱玩”：改错代码 -> 运行报错 -> 继续尝试错误的解法 -> 陷入死循环出不来。
- 🗑️ **盲目自信** - 有时候会信誓旦旦地删掉你有用的代码，或者引入根本不存在的库（幻觉）。
- 🧠 **遗忘症** - 上下文太长时，前面定好的规则转头就忘，强行“大聪明”。

<br>
<p class="text-xl text-center text-red-500 font-bold mt-4">总结：是个好工具，但得“牵着绳子溜”，不能完全放养！</p>

---
layout: center
class: text-center
---

# AI CLI 常用命令大赏

掌握核心命令，避免被 AI 带进沟里

---
layout: default
---

# 常用命令 1：进入交互模式

最常用的“主城”入口，开启沉浸式对话。

```bash
# 启动命令
coco
# 或者 claude
```

**📌 介绍：**
不带任何参数执行，直接在当前目录下进入沉浸式的 REPL（交互式）会话环境。

**💡 为什么常用（原因）：**
- 它是所有复杂操作的起点。在这个模式下，AI 可以保留你们持续对话的上下文。
- 适合进行排查 Bug、重构大规模代码、分析项目结构等需要 **反复拉扯** 的“重型任务”。
- 你可以随时跟它确认当前进度，及时打断它的错误行为。

---
layout: default
---

# 常用命令 2：`/commit` (一键提交)

拯救起名废的究极魔法。

```bash
# 在交互模式内执行，或外部直接 coco /commit
/commit
```

**📌 介绍：**
读取当前 Git 的暂存区（Staged）变更，自动分析修改内容并生成符合规范的 Commit Message，然后直接提交。

**💡 为什么常用（原因）：**
- **解放双手**：没人喜欢绞尽脑汁写 Commit Message。
- **杜绝废话**：告别 `git commit -m "update"` 或 `"fix bug"` 这种毫无营养的提交记录。
- **统一规范**：生成的描述往往比人类写的更清晰、更结构化，完美契合团队的 Git 规范。

---
layout: default
---

# 常用命令 3：`/review` (代码审查)

不知疲倦的无情“橡皮鸭”和严格的 Tech Lead。

```bash
# 审查当前改动
/review
```

**📌 介绍：**
让 AI 对当前的 Git 变更或者指定的文件进行 Code Review，指出潜在的安全隐患、性能瓶颈或者逻辑漏洞。

**💡 为什么常用（原因）：**
- **提前排雷**：在提 PR / MR 之前给自己上一道保险，把 Bug 扼杀在摇篮里。
- **细致入微**：它经常能抓到一些人类 Review 时容易忽略的细节（如：并发数据竞争、内存泄漏风险、忘记处理的 Edge Case）。
- 不用苦苦求着同事帮你看代码，随时随地获取建议。

---
layout: default
---

# 常用命令 4：`/clear` (清空上下文)

拯救幻觉与账单的物理超度大法。

```bash
# 感觉 AI 开始犯傻时果断敲下
/clear
```

**📌 介绍：**
强制重置当前会话的上下文记录，让 AI “失忆”，清空之前的对话历史。

**💡 为什么常用（原因）：**
- **防拉胯（防死循环）**：当对话过长，AI 开始胡言乱语、反复修改同一处正确代码时，说明它已经被旧的上下文带偏了，此时果断清空。
- **省钱**：长上下文等于烧钱，在完成一个独立任务后清空历史，可以大幅降低下一次对话的 Token 消耗。
- 贯彻“一事一议”原则，保持会话的专注度。

---
layout: center
class: text-center
---

# 感谢聆听！

避开“拉”的坑，发挥“夯”的力。
欢迎提问与交流！

*报告人：guoysh | 日期：5月15日*