

class ORM_Calculation():
    __lift_performed = {}

    def __init__(self, body_weight):
        self.body_weight = body_weight

    def strength_reps(self, start_reps, end_reps):
        return "You have increased your rep strength by %sx or %s Percent" % (end_reps / start_reps,
                                                                         int(((end_reps - start_reps)/start_reps)*100))

    def one_rep_max(self, reps, weight, lift):
            return "Your one rep max on %s is %slbs" % (lift, int(weight/(1.0278-(.0278*reps))))

    def total_lifts(self):
        return self.__class__.__lift_performed

    def add_lift(self, lift, orm):
        self.total_lifts()[lift] = int(orm)

    def __calc_lift_over_bodyweight(self, lift):
        return [self.total_lifts()[lift] - self.body_weight, round(self.total_lifts()[lift] / self.body_weight, 2)]

    def pound_for_pound(self):
        calculation = self.__calc_lift_over_bodyweight
        return ["Your one rep max on %s is %s which is %slbs over or %sx your current body weight" % (key, val,
        calculation(key)[0], calculation(key)[1]) for key, val in self.__class__.__lift_performed.items()]

    def add_total_weight(self, lift1, lift2, lift3):
        total_weight = sum([self.total_lifts()[lift1], self.total_lifts()[lift2], self.total_lifts()[lift3]])
        if total_weight > 1000:
            return "Your in the 1000lbs club at %slbs!" % total_weight
        else:
            return "Your getting there, just a little more. You are at %slbs" % total_weight

