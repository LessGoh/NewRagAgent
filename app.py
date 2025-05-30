import streamlit as st

st.title("🤖 Тест импортов")

# Тест 1: Базовые импорты
try:
    import os
    st.success("✅ os импортирован")
except Exception as e:
    st.error(f"❌ os: {e}")

# Тест 2: Проверка текущей директории
st.write(f"Текущая директория: {os.getcwd()}")

# Тест 3: Список файлов
try:
    files = os.listdir('.')
    st.write("Файлы в корне:", files)
except Exception as e:
    st.error(f"❌ Ошибка чтения файлов: {e}")

# Тест 4: Проверка папки agents
try:
    if os.path.exists('agents'):
        agent_files = os.listdir('agents')
        st.write("Файлы в agents/:", agent_files)
    else:
        st.error("❌ Папка agents не найдена!")
except Exception as e:
    st.error(f"❌ Ошибка agents: {e}")

# Тест 5: Проверка конкретного файла
try:
    if os.path.exists('agents/finance_agent.py'):
        st.success("✅ agents/finance_agent.py найден")
    else:
        st.error("❌ agents/finance_agent.py НЕ найден!")
except Exception as e:
    st.error(f"❌ Ошибка проверки файла: {e}")

# Тест 6: Попытка импорта
try:
    import sys
    sys.path.append('.')
    from agents.finance_agent import FinanceAnalysisAgent
    st.success("✅ FinanceAnalysisAgent импортирован успешно!")
except Exception as e:
    st.error(f"❌ Ошибка импорта: {e}")
