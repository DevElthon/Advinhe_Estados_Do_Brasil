import pandas as pd
import turtle
import patch_turtle_image

screen = turtle.Screen()
screen.title("Estados Brasucas")
screen.bgpic("Brazil_States.jpg")

def create_brazil_states_table():
    data_dict = {
        "State": ["Amazonas", "Roraima", "Para", "Amapa", "Acre","Rondonia",
                  "Mato Grosso", "Maranhao", "Tocantins", "Goias",
                  "Mato Grosso do Sul", "Piaui", "Bahia", "Minas Gerais",
                  "Sao Paulo","Parana", "Santa Catarina", "Rio Grande do Sul",
                  "Ceara","Rio Grande do Norte", "Paraiba", "Pernambuco",
                  "Alagoas", "Sergipe","Espirito Santo", "Rio de Janeiro"],
        "x": [-155.0, -99.0, 23.0, 40.0, -211.0, -123.0, -21.0, 132.0, 86.0,
              58.0,-11.0, 163.0, 170.0, 132.0, 67.0, 24.0, 43.0, -4.0, 206.0,
              256.0, 250.0, 244.0,253.0, 237.0, 178.0, 146.0],
        "y": [154.0, 240.0, 141.0, 228.0, 72.0, 56.0, 22.0, 130.0, 54.0, -23.0,
              -86.0,83.0, 19.0, -60.0, -118.0, -143.0, -190.0, -221.0, 123.0,
              106.0, 85.0, 60.0,47.0, 35.0, -92.0, -128.0]
    }

    df = pd.DataFrame(data_dict)
    df.to_csv("estados_do_brasil.csv")

def get_mouse_click_coor(x, y):
    print(x,y)

#create_brazil_states_table()
#turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("estados_do_brasil.csv")
all_states = data.State.to_list()
guessed_states = []

while len(guessed_states) < 26:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/26 estados encontrados", prompt="Qual o nome do estado?")

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("estados_para_aprender.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.State.item(), align="center")

