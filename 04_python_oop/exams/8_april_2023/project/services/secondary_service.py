from project.services.base_service import BaseService


class SecondaryService(BaseService):
    _CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self._CAPACITY)

    def details(self):
        robots_str = ' '.join([bot.name for bot in self.robots]) if self.robots else 'none'
        info = [
            f'{self.name} Secondary Service:',
            f'Robots: {robots_str}'
        ]
        return '\n'.join(info)