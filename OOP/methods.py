class dog:
    def __init__(details,color,action):
        details.color=color
        details.action=action
    def Attribute(details):
        print("The",details.color,"Dog is",details.action)
dog1 = dog("Black","Barking")
dog1.Attribute()