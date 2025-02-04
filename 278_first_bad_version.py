// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int first = 1, last = n;
        while (first < last) {  // Use `first < last` to simplify the condition
            int mid = first + (last - first) / 2;
            if (isBadVersion(mid)) {
                last = mid;  // Narrow down to the left half
            } else {
                first = mid + 1;  // Narrow down to the right half
            }
        }
        return first;  // First will point to the first bad version
    }
