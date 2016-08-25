#include <iostream>

using namespace std;

float processLine3(string const & line, int b, int e) {
	auto temp = line.substr(b, e - b);
	return stoi(temp);
}

float processLine2(string const & line, int b, int e) {
	for (int i = b; i < e; ++i) {
		if (line[i] == '*') {
			return processLine3(line, b, i) * processLine2(line, i + 1, e);
		}
		if (line[i] == '/') {
			return processLine3(line, b, i) / processLine2(line, i + 1, e);
		}
	}
	processLine3(line, b, e);
}

float processLine(string const & line, int b, int e) {
	for (int i = b; i < e; ++i) {
		if (line[i] == '+') {
			return processLine2(line, b, i) + processLine(line, i + 1, e);
		}
		if (line[i] == '-') {
			return processLine2(line, b, i) - processLine(line, i + 1, e);
		}
	}
	processLine2(line, b, e);
}

float processLine(string const & line) {
	return processLine(line, 0, line.length());
}

int main() {
	cout << processLine("2+22/3-2*2*2");
}
