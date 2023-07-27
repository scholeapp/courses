# 改行関係のない40文字.
# o: 荷物
# O: ゴールの上の荷物
# p: プレイヤー
# P: ゴールの上のプレイヤー
# .: ゴール
# #: 壁
soko = \
'########'\
'# .. p #'\
'# oo   #'\
'#      #'\
'########'

width = 8
height = 5

# sokoのix番目をcにする関数
def update_soko(ix, c):
    global soko
    soko = soko[:ix] + c + soko[ix+1:]

def main():
    while True:
        # 描画
        draw()
        # ゲームをクリアしてるか
        if not is_still_solving():
            break

        command = input('w: up, a: left, s: down, d: right. command?: ')
        update(command)
    print('Congratulations!')


def draw():
    for y in range(height):
        for x in range(width):
            cell = soko[y*width + x]
            print(cell, end='')
        print()
def is_still_solving():
    still_solving = False
    for ix in range(width * height):
        if soko[ix] == 'o':
            still_solving = True
    return still_solving

def update(command):
    # update soko
    dx = 0
    dy = 0
    if command == 'w':
        dy = -1
    elif command == 'a':
        dx = -1
    elif command == 's':
        dy = 1
    elif command == 'd':
        dx = 1
    # プレイヤーのindex
    ix = -1
    for ix in range(width * height):
        if soko[ix] == 'p' or soko[ix] == 'P':
            break
    x = ix % width  # xはixを幅で割ったあまり
    y = ix // width  # yはixを幅で割った商
    
    # プレイヤーの移動先
    next_x = x + dx
    next_y = y + dy

    # 境界チェック
    if next_x < 0 or next_y < 0 or next_x >= width or next_y >= height:
        return

    next_ix = next_y * width + next_x
    if soko[next_ix] == ' ' or soko[next_ix] == '.':
        # プレイヤーが移動先に移動できる
        if soko[next_ix] == '.':
            update_soko(next_ix, 'P')
        else:
            update_soko(next_ix, 'p')
        if soko[ix] == 'P':
            update_soko(ix, '.')
        else:
            update_soko(ix, ' ')
    elif soko[next_ix] == 'o' or soko[next_ix] == 'O':
        # 移動先が荷物なので、その荷物を移動できるか調べる
        next_next_x = next_x + dx
        next_next_y = next_y + dy

        if next_next_x < 0 or next_next_y < 0 or next_next_x >= width or next_next_y >= height:
            return
        next_next_ix = next_next_y * width + next_next_x
        if soko[next_next_ix] == ' ' or soko[next_next_ix] == '.':
            # 荷物を動かせるとき
            if soko[next_next_ix] == '.':
                # 2つ先の荷物の行き先がゴールの上
                update_soko(next_next_ix, 'O')
            else:
                update_soko(next_next_ix, 'o')
            if soko[next_ix] == 'O':
                # 1つ先の荷物がゴールの上
                update_soko(next_ix, 'P')
            else:
                update_soko(next_ix, 'p')
            if soko[ix] == 'P':
                # プレイヤーのいるところがゴール
                update_soko(ix, '.')
            else:
                update_soko(ix, ' ')

main()