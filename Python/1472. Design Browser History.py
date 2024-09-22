class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.page = 0

    def visit(self, url: str) -> None:
        if len(self.history) - 1 > self.page:
            del self.history[self.page + 1::]
        self.history.append(url)
        self.page += 1

    def back(self, steps: int) -> str:
        if steps >= self.page:
            self.page = 0
        else:
            self.page = self.page - steps
        return self.history[self.page]

    def forward(self, steps: int) -> str:
        if steps + self.page + 1 >= len(self.history):
            self.page = len(self.history) - 1
        else:
            self.page = self.page + steps
        return self.history[self.page]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)