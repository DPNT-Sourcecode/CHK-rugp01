
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name) -> str:
        if friend_name:
            return f"Hello, {friend_name}!"
        return "Hello, World!"
