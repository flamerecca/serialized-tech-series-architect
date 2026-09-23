#!/usr/bin/env python3
"""將一份 SVG 檔案轉換成 PNG 圖片。

用途：視覺代理人 (visual-agent) 產出的架構圖、資料視覺化、封面插圖，轉譯結果
以 SVG 原始碼呈現；使用者若需要實際可交付的點陣圖檔，這支腳本負責把 SVG
轉換成 PNG，不負責繪製或修改 SVG 內容本身。

轉換工具依序嘗試 rsvg-convert、Inkscape、ImageMagick，PATH 裡找到哪一個就用
哪一個，全部找不到時報錯並提示需安裝其中一種。

用法：
    python3 svg_to_png.py 輸入.svg 輸出.png
    python3 svg_to_png.py 輸入.svg 輸出.png --scale 2
    python3 svg_to_png.py 輸入.svg 輸出.png --width 1200 --height 630
    python3 svg_to_png.py 輸入.svg 輸出.png --background white

參數：
    input_svg         輸入 SVG 檔案路徑
    output_png         輸出 PNG 檔案路徑
    --width             輸出寬度，單位 px，與 --height 需成對指定
    --height            輸出高度，單位 px，與 --width 需成對指定
    --scale             縮放倍率，預設 2，未指定 --width/--height 時生效，
                        用於產出 Retina 螢幕適用的高解析度點陣圖
    --background        背景色，預設維持 SVG 原本的透明背景，例如封面圖需要
                        不透明底色時可傳入 white 或 #ffffff
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def build_rsvg_convert_command(binary, input_svg, output_png, width, height, scale, background):
    cmd = [binary, str(input_svg), "-o", str(output_png)]
    if width and height:
        cmd += ["-w", str(width), "-h", str(height)]
    else:
        cmd += ["-z", str(scale)]
    cmd += ["-b", background if background else "none"]
    return cmd


def build_inkscape_command(binary, input_svg, output_png, width, height, scale, background):
    cmd = [binary, str(input_svg), "--export-type=png", f"--export-filename={output_png}"]
    if width and height:
        cmd += [f"--export-width={width}", f"--export-height={height}"]
    else:
        cmd += [f"--export-dpi={int(96 * scale)}"]
    if background:
        cmd += [f"--export-background={background}", "--export-background-opacity=255"]
    return cmd


def build_imagemagick_command(binary, input_svg, output_png, width, height, scale, background):
    cmd = [binary]
    cmd += ["-background", background if background else "none"]
    if not (width and height):
        cmd += ["-density", str(int(96 * scale))]
    cmd += [str(input_svg)]
    if width and height:
        cmd += ["-resize", f"{width}x{height}!"]
    cmd += [str(output_png)]
    return cmd


CONVERTERS = [
    ("rsvg-convert", build_rsvg_convert_command),
    ("inkscape", build_inkscape_command),
    ("magick", build_imagemagick_command),
    ("convert", build_imagemagick_command),
]


def find_converter():
    for name, builder in CONVERTERS:
        binary = shutil.which(name)
        if binary:
            return name, binary, builder
    return None


def main():
    parser = argparse.ArgumentParser(description="將一份 SVG 檔案轉換成 PNG 圖片")
    parser.add_argument("input_svg", type=Path)
    parser.add_argument("output_png", type=Path)
    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--background", type=str, default=None)
    args = parser.parse_args()

    if bool(args.width) != bool(args.height):
        print("錯誤：--width 與 --height 須成對指定，不能只給其中一個", file=sys.stderr)
        return 1

    if not args.input_svg.exists():
        print(f"錯誤：找不到輸入檔案 {args.input_svg}", file=sys.stderr)
        return 1

    found = find_converter()
    if not found:
        print(
            "錯誤：系統裡找不到任何可用的轉換工具，"
            "請安裝 rsvg-convert、Inkscape 或 ImageMagick 其中一種後再試一次。\n"
            "macOS 可用 Homebrew 安裝：brew install librsvg",
            file=sys.stderr,
        )
        return 1

    name, binary, builder = found
    args.output_png.parent.mkdir(parents=True, exist_ok=True)
    cmd = builder(binary, args.input_svg, args.output_png, args.width, args.height, args.scale, args.background)

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"錯誤：使用 {name} 轉換失敗\n{result.stderr}", file=sys.stderr)
        return 1

    if not args.output_png.exists():
        print(f"錯誤：{name} 執行完成但沒有產生輸出檔案 {args.output_png}", file=sys.stderr)
        return 1

    print(f"轉換完成，使用 {name}：{args.input_svg} -> {args.output_png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
