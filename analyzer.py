# OSN Global Security Data Analyzer
# A tool to analyze word frequency in security reports.

def analyze_trends(data):
    words = data.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

report = "Middle East security trends show increased activity in global monitoring."
print("Top Trends:", analyze_trends(report))
