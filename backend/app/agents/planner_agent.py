class PlannerAgent:

    def decompose(self, goal):
        return [
            "Analyze symptoms",
            "Check possible diagnosis",
            "Suggest medications",
            "Recommend lifestyle changes"
        ]

    def create_plan(self, steps):
        return "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])

    def run(self, goal):
        steps = self.decompose(goal)
        plan = self.create_plan(steps)
        return plan