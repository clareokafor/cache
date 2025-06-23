# Cache Management Application

## Overview

This project implements a basic application for managing a cache with a fixed capacity. The system is designed to handle incoming page requests and manage the cache according to one of two strategies:

- **FIFO (First-In, First-Out):** When the cache is full, the page that has been in the cache the longest is evicted.
- **LFU (Least Frequently Used):** When the cache is full, the page that has been used least often is removed.

The goal of this application is to efficiently handle page requests while respecting the cache’s predetermined capacity. Each page request is processed by checking whether it is already present in the cache. If it is not found (a cache miss) and the cache is full, the application selects a page to evict based on the chosen strategy. Once the eviction policy finishes processing all requests, the final state of the cache is displayed.

---

## Features

- **Request Input:**  
  Users are prompted to enter page numbers that are added to a request list. Entering `0` stops the entry process.

- **FIFO Eviction Policy:**  
  - Checks if a requested page is in the cache.
  - If it is not and the cache is not yet full, the page is simply added.
  - If the cache is full, the page that has resided in the cache for the longest time (the first page in the list) is evicted before adding the new page.

- **LFU Eviction Policy:**  
  - Tracks the frequency of page requests.
  - If a requested page is not in the cache and the cache is full, the page with the lowest frequency count is evicted before adding the new page.
  - When a requested page is already in the cache, its frequency count is increased.

- **Cache Display:**  
  Once all requests have been processed (or the specified eviction policy completes), the final state of the cache is printed to the screen.

---

## Implementation Details

- **Global Data Structures:**  
  - `cache`: A list representing the cache memory with a fixed capacity (e.g., 8 pages).
  - `requests`: A list that holds all page numbers entered by the user.
  - `number_in_requests`: A dictionary to track the frequency of page requests (used primarily for the LFU policy).

- **User Input Loop:**  
  The program repeatedly prompts the user to enter a page number until a sentinel value (`0`) is provided. These values populate the `requests` list.

- **FIFO Function (`fifo`):**  
  Iterates through each page request. For each request, it checks if the page already exists in the `cache` (a hit) or not (a miss). On a miss, if the cache is full, the oldest page (first element) is removed before the new page is appended.

- **LFU Function (`lfu`):**  
  Processes each page request using a frequency dictionary to keep count. When the cache is full, the function evicts the least frequently used page (using a helper method to increase the count for repeated requests).

- **Helper Function (`increasingPageCount`):**  
  Increases the count of a page’s occurrence in the `number_in_requests` dictionary whenever a page is accessed.

---

## Future Enhancements

- **Enhanced Eviction Policies:**  
  Experiment with additional cache replacement strategies (e.g., LRU or a hybrid approach).
- **Improved Frequency Tracking:**  
  Refine the LFU implementation to handle cases where multiple pages share the same usage frequency.
- **User Interface:**  
  Consider developing a graphical user interface (GUI) or web interface to interact with the cache system.
- **Performance Reporting:**  
  Add logging and performance metrics to help analyze cache hit ratios over time.

---
[LICENSE](https://github.com/clareokafor/cache?tab=MIT-1-ov-file)
