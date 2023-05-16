#OGOCHUKWU JANE OKAFOR
#201666459

#Cache Management 
#Step 1: Creating a List of Requests

cache = []  #An empty global scope list with a maximum of 8 pages.

requests = [] #An empty global scope list with 8 or more than 8 pages.

number_in_requests = {}

#How do add pages to the cache memory? First, we need to add pages to the request list.
#How do we add pages to the request list? Here, a user will be asked to input page numbers to the request list.

while True:
    pages = int(input("Enter page number: ")) #This tells a user to input a page number.
    if pages == 0: #If a user has achieved his/her desired numbers of pages, the user presses 0.
        break 
    requests.append(pages)

print(requests) #This will show the number of pages the user has added to the request list.

#Step 2: Determining the Ways of Adding Pages to the Cache List and Ways of Calling for Eviction
# A page can be kicked out of the cache memory and replaced by another using fifo and lfu.

#A user can use the FIFO function to kick out a page that has been on the cache for the longest.
def fifo():
    for page in requests:
        if page in cache: 
            print("Hit") #The page number will not be added since it already exists in the cache.

        else:
            print("Miss") #Add the page number to the cache.
            if len(cache) < 8: #If the page has a minimum of 8 pages.
                cache.append(page) #Add page number from 
            else:
                len(cache) >= 8 #If the cache is full
                cache.pop(0) #The first page on the list will be removed.
                cache.append(page) #A new page will be added to the cache.
    print(cache)
    print(requests)
    cache.clear()
    requests.clear()
    print("The final state of cache", cache)


#A user can use the LFU function to kick duplicate pages and evict a least frequently used page.
def lfu():
    for i in range(len(requests)):
        if requests[i] not in cache:
            print("Miss")
            
            if len(cache) == 8: #cache is full
                cache_num = {}
                leastUsedNums = []
                
                for page in cache:
                    if page in number_in_requests.keys():
                        cache_num[page] = number_in_requests[page]

                minimumPage = min(cache_num.values())
                
                for key in cache_num.keys():
                    if cache_num[key] == minimumPage:
                        leastUsedNums.append(key)

                cache.remove(min(leastUsedNums))
                cache.append(requests[i])
            
            else:
                cache.append(requests[i])

        else:
            print("Hit")
            increasingPageCount(requests[i])
    
    print(cache)
    cache.clear()
    requests.clear()
    return None

def increasingPageCount(value):
    if value not in number_in_requests.keys():
        number_in_requests[value] =1
     
    else:
        number_in_requests +=1
           
#Step 3: Calling for the implementation of FIFO and LFU as well as Q's Eviction.               
#If a user input's Q, he or she will exit the program.
#Lets make use "user_choice" to serve as a function to determine the input a user will choose for the program.
user_choice = input("Press 1 for fifo, or press 2 for lfu, or  press Q to quit the program: ")

if user_choice == "1": #Fifo function will be implemented if a user enters 1
    fifo()

elif user_choice == "2": #Lfu function will be implemented if a user enter 2
    lfu()

elif user_choice == "Q": #User will quits or exits the program by entering Q.
    exit() 





