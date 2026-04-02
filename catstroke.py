def calculate_height_cm(keystrokes: int, energy_per_keystroke: float, cat_mass_kg: float) -> float:
    """
    キーストローク数から、指定した重さの猫を何cm持ち上げられるか計算する。
    仕事量 W = mgh より h = W / (m * g)
    """
    g = 9.8  # 重力加速度 (m/s^2)
    total_energy_joule = keystrokes * energy_per_keystroke
    height_m = total_energy_joule / (cat_mass_kg * g)
    return height_m * 100  # cm に変換


def comment_for_height(height_cm: float) -> str:
    if height_cm < 0.5:
        return "微動だにせず"
    if height_cm < 1:
        return "ほんの少し動いた…気がする"
    if height_cm < 10:
        return "やっと浮いた"
    if height_cm < 30:
        return "持ち上がってる！"
    if height_cm < 500:
        return "かなり浮いた！"
    return "猫、ガチで困惑"


def main() -> None:
    energy_per_keystroke = 0.02  # 1打鍵あたりのエネルギー（J）※ネタ用の仮定

    cats = [
        ("子猫", 2.0),
        ("猫", 4.0),
        ("デブ猫", 7.0),
    ]

    print("=== 猫持ち上げ換算CLI ===")
    print("今日のキーストローク数を入力すると、")
    print("そのエネルギーで猫を何cm持ち上げられるか計算します。")
    print()

    while True:
        user_input = input("今日のキーストローク数を入力してください: ").strip()

        try:
            keystrokes = int(user_input)
            if keystrokes < 0:
                print("0以上の整数を入力してください。")
                continue
            break
        except ValueError:
            print("整数で入力してください。")
            continue

    print()
    print(f"キーストローク数: {keystrokes:,} 回")
    print(f"総エネルギー: {keystrokes * energy_per_keystroke:.2f} J")
    print()
    print("あなたは今日……")
    print("-" * 36)

    for cat_name, cat_mass in cats:
        height_cm = calculate_height_cm(keystrokes, energy_per_keystroke, cat_mass)
        comment = comment_for_height(height_cm)
        print(f"{cat_name:>4} ({cat_mass:.1f}kg): {height_cm:>7.2f} cm  | {comment}")

    print("-" * 36)


if __name__ == "__main__":
    main()