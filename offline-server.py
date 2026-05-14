#!/usr/bin/env python3
"""离线运行 Slidev 静态构建，支持 presenter 等前端路由。"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import os


class SlidevHandler(SimpleHTTPRequestHandler):
    """找不到静态文件时回退到 index.html。"""

    def do_GET(self):
        requested = Path(self.translate_path(self.path))
        if not requested.exists() and "." not in Path(self.path).name:
            self.path = "/index.html"
        return super().do_GET()


def main():
    """启动本地静态服务。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=3031)
    parser.add_argument("--dir", default="dist")
    args = parser.parse_args()

    root = Path(args.dir).resolve()
    if not (root / "index.html").exists():
        raise SystemExit(f"找不到 {root / 'index.html'}，请先运行 npm run build")

    os.chdir(root)
    server = ThreadingHTTPServer((args.host, args.port), SlidevHandler)
    print(f"Slidev offline: http://{args.host}:{args.port}/")
    print(f"Presenter mode: http://{args.host}:{args.port}/presenter/")
    server.serve_forever()


if __name__ == "__main__":
    main()
