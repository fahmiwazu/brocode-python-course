############ method chaining in python
class Car:

    def turn_on(self):
        print("urip")
        return self

    def drive(self):
        print("gass")
        return self

    def brake(self):
        print("remm")
        return self

    def turn_off(self):
        print("mati")
        return self

sedan = Car()
# sedan.turn_on().drive()
# sedan.brake().turn_off()
# sedan.turn_on().drive().brake().turn_off()

(sedan
 .turn_on()
 .drive()
 .brake()
 .turn_off())