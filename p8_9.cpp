#include <iostream>
#include <vector>

using namespace std;

void buildParents(string const & prefix, int toOpen, int toClose, vector<string> & storage) {
	if (toOpen == 0 && toClose == 0) {
		storage.push_back(prefix);
		return;
	}

	if (toOpen > 0) {
		buildParents(prefix + "(", toOpen - 1, toClose + 1, storage);
	}

	if (toClose > 0) {
		buildParents(prefix + ")", toOpen, toClose - 1, storage);
	}
}


vector<string> getParents(int n) {
	vector<string> storage;
	buildParents("", n, 0, storage);
	return storage;
}

int main() {
	auto strings = getParents(3);
	for (auto const & s : strings) {
		std::cout << s << " ";
	}
}
