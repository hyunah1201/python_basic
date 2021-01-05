names = ["Jin", "Sungchul", "Ronaldo", "Hong", "Seo"]
positions = ["MF","DF", "CF", "WF", "GK"]
numbers = [10, 15, 20, 3, 1]

players = [[name, position, number ]for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

class SoccerPlayer(object):
    # 생성자
    def __init__(self, name, position, back_number):
        # 속성들
        self.name = name
        self.position = position
        self.back_number = back_number

    # back_number 속성을 변경하는 메서드
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center " % (self.name, self.position)

player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_objects[0])