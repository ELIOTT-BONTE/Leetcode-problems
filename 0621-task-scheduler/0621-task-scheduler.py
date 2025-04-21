from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task using a Counter
        count = Counter(tasks)  # e.g., {'A': 3, 'B': 2}

        # Step 2: Create a max-heap using negative frequencies
        # heapify expects a list, and we need to use heapq.heapify
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        # Step 3: Initialize a queue (deque) to keep track of tasks in cooldown
        # Each element will be a tuple (available_time, remaining_count)
        queue = deque()

        # Step 4: Initialize time counter
        time = 0

        # Step 5: Simulate each time unit
        while heap or queue:
            time += 1

            # b. If we can run a task, pop the most frequent one from heap
            if heap:
                current = heapq.heappop(heap)  # remember: these are negative counts
                current += 1  # reduce its (negative) count by 1 (e.g., -3 -> -2)

                # if it's not yet finished, add it to cooldown
                if current < 0:
                    # ready time is current time + cooldown
                    queue.append((time + n, current))

            # c. If a task has finished its cooldown, push it back to heap
            if queue and queue[0][0] == time:
                ready_time, task = queue.popleft()
                heapq.heappush(heap, task)

        # Step 6: Return total time
        return time
