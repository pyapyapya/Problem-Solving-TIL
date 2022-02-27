#include <iostream>
#include <algorithm>

using namespace std;

int arr[2][3];
int max_dp[2][3];
int min_dp[2][3];
int temp[3];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> temp[0] >> temp[1] >> temp[2];
		for (int j = 0; j < 3; j++) {
			if (i == 0) {
				arr[0][j] = temp[j];
				max_dp[i][j] = temp[j];
				min_dp[i][j] = temp[j];
			}
			else {
				arr[1][j] = temp[j];

			}
		}
		if (i == 0)
			continue;
			max_dp[1][0] = arr[1][0] + max(max_dp[0][0], max_dp[0][1]);
			max_dp[1][1] = arr[1][1] + max(max_dp[0][0], max(max_dp[0][1], max_dp[0][2]));
			max_dp[1][2] = arr[1][2] + max(max_dp[0][1], max_dp[0][2]);

			min_dp[1][0] = arr[1][0] + min(min_dp[0][0], min_dp[0][1]);
			min_dp[1][1] = arr[1][1] + min(min_dp[0][0], min(min_dp[0][1], min_dp[0][2]));
			min_dp[1][2] = arr[1][2] + min(min_dp[0][1], min_dp[0][2]);

			for (int j = 0; j < 3; j++) {
				arr[0][j] = arr[1][j];
				max_dp[0][j] = max_dp[1][j];
				min_dp[0][j] = min_dp[1][j];

				arr[1][j] = 0;
				max_dp[1][j] = 0;
				min_dp[1][j] = 0;
		}
	}
	cout << *max_element(max_dp[0], max_dp[0] + 3) << ' ' << *min_element(min_dp[0], min_dp[0] + 3);
}