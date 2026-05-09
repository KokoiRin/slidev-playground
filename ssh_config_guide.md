# 配置 GitHub SSH 密钥指南

如果在向 GitHub 推送代码时遇到 `Permission denied (publickey)` 错误，可以通过以下步骤配置 SSH 密钥。

## 1. 检查是否已有 SSH 密钥
首先，检查本地是否已经生成过 SSH 密钥。
```bash
ls -al ~/.ssh
```
*如果你看到类似 `id_rsa.pub`、`id_ed25519.pub` 的文件，说明你已经有密钥了，可以直接跳到第 3 步。*

## 2. 生成新的 SSH 密钥
如果没有密钥，使用以下命令生成一个新的（推荐使用 ed25519 算法）：
```bash
ssh-keygen -t ed25519 -C "你的邮箱@example.com"
```
*按回车键接受默认的文件路径。系统会提示你输入密码短语（passphrase），你可以直接按回车跳过（不设置密码），或者输入一个密码以增加安全性。*

## 3. 启动 ssh-agent 并添加密钥
启动 ssh-agent：
```bash
eval "$(ssh-agent -s)"
```

如果你使用的是 macOS，为了让 ssh-agent 记住密码（如果你设置了密码），你需要在 `~/.ssh/config` 文件中添加以下内容（如果没有该文件则创建它）：
```text
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

然后，将你的私钥添加到 ssh-agent 中：
```bash
# 如果你生成的是 ed25519 密钥：
ssh-add --apple-use-keychain ~/.ssh/id_ed25519

# 如果你使用的是旧的 rsa 密钥：
# ssh-add --apple-use-keychain ~/.ssh/id_rsa
```
*(注意：`--apple-use-keychain` 是 macOS 特有的参数，Linux/Windows 用户请直接使用 `ssh-add ~/.ssh/id_ed25519`)*

## 4. 将公钥添加到 GitHub
复制你的公钥内容。你可以使用 `pbcopy` 命令直接将其复制到剪贴板：
```bash
# 如果是 ed25519：
pbcopy < ~/.ssh/id_ed25519.pub

# 如果是 rsa：
# pbcopy < ~/.ssh/id_rsa.pub
```

然后按照以下步骤在 GitHub 上添加：
1. 登录 GitHub，点击右上角的头像，选择 **Settings**（设置）。
2. 在左侧边栏找到并点击 **SSH and GPG keys**。
3. 点击绿色的 **New SSH key** 按钮。
4. 在 **Title** 框中随便起个名字（比如 "MacBook Pro"）。
5. 在 **Key** 框中，`Cmd + V` 粘贴你刚才复制的公钥内容。
6. 点击 **Add SSH key** 保存。

## 5. 测试连接并推送代码
配置完成后，在终端中测试一下是否连接成功：
```bash
ssh -T git@github.com
```
*如果看到类似 `Hi KokoiRin! You've successfully authenticated...` 的信息，说明配置成功！*

现在你可以手动执行推送命令了：
```bash
git push -u origin main
```
