# Временная упрощенная версия для диагностики

class FinanceAnalysisAgent:
    """Упрощенный агент для тестирования"""
    
    def __init__(self):
        self.chat_history = []
    
    def chat(self, message: str) -> str:
        """Простой метод чата для тестирования"""
        return f"Тестовый ответ на: {message}"
    
    def get_chat_history(self):
        return self.chat_history
    
    def clear_history(self):
        self.chat_history = []
        
    def get_suggestions(self):
        return [
            "Тестовый вопрос 1",
            "Тестовый вопрос 2", 
            "Тестовый вопрос 3"
        ]
