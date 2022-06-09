def discussability(movies_array, friends_2d_array):
    """
    Function return dictionary with number of friends of user,
    who have already seen movie from movies_array,
    where keys - name of movie, and values - numbers.
    We also consider movies that haven't already seen.

    For ease of verification, we will denote the complexity of the program code from comment to comment
    So for example, for this function, the

    TIME COMPLEXITY: minimal - O(n+f), maximal - O(n*f)
                     where "n" is the number of movies and "f" is the number of friends.
    SPACE COMPLEXITY: O(n)
    """
    dictionary = dict.fromkeys(movies_array, 0)

    for friend in friends_2d_array:
        for movie in friend:
            dictionary[movie] += 1

    return dictionary


def uniqueness(movies_array, similarities_2d_array, friends_2d_array):
    """
    For the convenience of further work, we will create two dictionaries, 
    in the first of them we will designate each film with a number corresponding only to it. 
    The second dictionary is the opposite of this, 
    i.e. by the number you can understand which movie it stands for.

    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(n)
    """
    movie_number = dict()
    number_movie = dict()
    graph = []
    for i in range(len(movies_array)):
        movie_number[movies_array[i]] = i
        number_movie[i] = movies_array[i]
        graph.append([])

    """
    Two subsequent cycles create a graph represented as an adjacency list. 
    At the same time, the films are already presented in digital form in the graph.
    
    TIME COMPLEXITY: minimal - O(x*y), maximal - O(x*y^2), where 'x' is the number of lists inside 
                     the similarities array, and 'y' is the number of similarities inside the list of lists
                     !!! IMPORTANT: By the way, the algorithm is implemented in such a way that it takes into 
                     account not only pairwise similarities, in this regard, 
                     another maximum time complexity appears.
    SPACE COMPLEXITY: minimal - O(x*y), maximal - O(x*y^2). Similarly with time complexity.
    """
    similarity = []
    for similarities_1d_array in range(len(similarities_2d_array)):
        similarity.append([])
        for movie in range(len(similarities_2d_array[similarities_1d_array])):
            similarity[similarities_1d_array]\
                .append(movie_number[similarities_2d_array[similarities_1d_array][movie]])

    for similarities_1d_array in range(len(similarity)):
        for movie in range(len(similarity[similarities_1d_array])):
            graph[similarity[similarities_1d_array][movie]]\
                .extend(similarity[similarities_1d_array][:movie]
                        + similarity[similarities_1d_array][movie+1:])

    """
    Depth First Search algorithm included to search all components of the graph.
    The result of the following code is a list of graph components, 
    with lists of vertices (in digital form) that are included in the component.
    
    TIME COMPLEXITY: sum of edges from each vertex = 2 * O(n) = O(n)
    SPACE COMPLEXITY: O(n)
    """
    def dfs(vertex):
        visited[vertex] = True
        for u in graph[vertex]:
            if not visited[u]:
                movies_in_components[-1].append(u)
                dfs(u)

    n = len(graph)
    movies_in_components = []
    visited = [False for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            movies_in_components.append([v])
            dfs(v)

    """
    The following code finds the intersection of each movie of the graph with components, 
    if there is an intersection, then there are similar movies in this component.
    In particular, the method of storing information is immediately organized: 
    how many friends seen similar movies. In the form of dictionaries in the dictionary. 
    If none, then the dictionary of similar films is empty.
    
    TIME COMPLEXITY: minimal - O(c*n), maximal - O(n^2), where 'c' - number of components
    SPACE COMPLEXITY: O(n^2)
    
    It is quite difficult to determine the asymptotic complexity of the code here.
    """
    dictionary = {number_movie[movie]: {} for movie in range(len(graph))}
    for movie in range(len(graph)):
        for component in movies_in_components:
            if len(set(component).intersection(set(graph[movie]))) > 0:
                dictionary[number_movie[movie]] = {number_movie[el]: 0 for el in set(component)-{movie}}
                break

    """
    And here, just the same, there is a calculation for each movie, 
    how many friends seen similar movies.
    And adding information to our unified dictionary.
    
    TIME COMPLEXITY: minimal - O(f+n), maximal - O(n^2)
    SPACE COMPLEXITY: O(n)
    """
    seen_movies = dict()
    for friend in friends_2d_array:
        for movie in friend:
            if movie not in seen_movies:
                seen_movies[movie] = 1
            else:
                seen_movies[movie] += 1

    for movie in dictionary:
        for movie_arr_el in dictionary[movie]:
            dictionary[movie][movie_arr_el] = seen_movies.setdefault(movie_arr_el, 0)

    """
    Find the mean values.
    
    TIME COMPLEXITY: minimal - O(n), maximal - O(n^2)
    SPACE COMPLEXITY: -
    """
    for movie in dictionary:
        if len(dictionary[movie].values()) == 0:
            dictionary[movie] = 0
        else:
            dictionary[movie] = sum(dictionary[movie].values()) / len(dictionary[movie].values())

    return dictionary


def total(movies_array, similarities_array, friends_array):
    """
    Now let's find the overall result, i.e. the film that we will recommend.
    To do this, call the discussability and uniqueness functions, and divide one by the other.
    Of course, given the rules of division. If it is divided by zero, then we assign 0 points to the film.
    Then we find the maximum score. This will be our recommended movie.
    ------------------------------------------------------------------------------------------------------
    TOTAL TIME COMPLEXITY for our program:
        minimal = O(x*y) + O(c*n)
        maximal = O(n*f) + O(x*y^2) + O(c*n^2)
    TOTAL SPACE COMPLEXITY for our program:
        minimal = O(x*y) + O(n^2)
        maximal = O(x*y^2) + O(n^2), where "n" - is the number of movies;
                                           "f" - is the number of friends;
                                           'x' - is the number of lists inside the similarities array;
                                           'y' - is the number of similarities inside the list of lists;
                                           'c' - is the number of components.
    """
    _uniqueness = uniqueness(movies_array, similarities_array, friends_array)
    _discussability = discussability(movies_array, friends_array)

    for movie in _uniqueness:
        if _uniqueness[movie] == 0:
            _discussability[movie] = 0
        else:
            _discussability[movie] = _discussability[movie] / _uniqueness[movie]
    return max(_discussability, key=_discussability.get)


# Example 1, your input data

movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker"]
similarities = [["Parasite", "1917"],
                ["Parasite", "Jojo Rabbit"],
                ["Joker", "Ford v Ferrari"]]
friends = [["Joker"],
           ["Joker", "1917"],
           ["Joker"],
           ["Parasite"],
           ["1917"],
           ["Jojo Rabbit", "Joker"]]


# Example 2, which I described in the second paragraph of the previous written assignment.

# movies = [1,2,3,4,5,6,7]
# similarities = [[1,2,3],
#                 [4,5],
#                 [6,5],
#                 [7,1]]
# friends = [[1,3],
#            [2],
#            [4],
#            [6,7,1],
#            [4]]

print(total(movies, similarities, friends))
