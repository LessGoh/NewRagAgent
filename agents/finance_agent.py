# Упрощенная версия agents/finance_agent.py

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
            "Покажи мне стратегии связанные с RSI",
            "Сравни MACD и Bollinger Bands", 
            "Найди исследования по algorithmic trading"
        ]
