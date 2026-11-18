class Rrt:
    """
    A class functions that implement an improved RRT sampling-based planner.
    """
    def __init__(self,world,x_start):
        """
        Stores the arguments as internal attributes, and initializes an
        attribute   graph of class   Graph containing a single node at
        x_start.
        """
        pass  # Substitute with your code
        
    
    def local_planner_steer(self,x_near,x_sample,{}max_dist{}):
        """
        Generate a new point   x_steer by moving an incremental distance
        max_dist from   x_near in the direction of   x_sample. If the distance
        between   x_near and   x_sample is less than   max_dist, then
        x_steer=x_sample.
        """
        pass  # Substitute with your code
        return x_steer
    
    def local_planner_is_collision(self,{}x_edge1{},{}x_edge2{},{}max_dist_edge_check{}):
        """
        Generates   nb_points equispaced points on the line between   x_edge1
        and   x_edge2, such that the maximum distance between two consecutive
        samples is less than   max_dist_edge_check. Note that the value of
        nb_points is determined by the distance between the two points and
        max_dist_edge_check.
        """
        pass  # Substitute with your code
        return flag
    
    def extend(self):
        """
        The function performs the following steps:
         - it:sampleState Use world.sample to generate a collision-free sample
        location   x_sample; ensure that the parameter   size is large enough to
        cover the entire space.
         - Use graph.nearest_neighbors (with   k_neighbors=1) to find the index
         idx_near of the single closest neighbor of   x_sample. Assign the
        coordinates corresponding to   idx_near to a variable   x_near.
         - Use local_planner_steer to generate   x_steer from   x_near,
        x_sample.
         - Use local_planner_is_collision to check whether   x_near can be
        connected to   x_steer. If there is no collision, add   x_steer to
        graph.graph_vector, setting its backpointer to   idx_near, and updating
        the   neighbor and   neighbor_cost fields of
        self.graph.graph_vector[idx_near].
         - Repeat from  it:sampleState until a sample is successfully added, or
        up to 100 times.
        """
        pass  # Substitute with your code
        return {}x_steer{}
    
    def search(self,{}x_start{},{}x_end{},{}goal_dist_threshold{}):
        """
        Implement a tree-based sampling search algorithm. The function performs
        the following steps:
         - it:extend Call extend to grow the tree with a new sample with
        location   x_steer.
         - If the distance between   x_steer and   x_end is less then
        goal_dist_threshold, call local_planner_is_collision to try to connect
        the goal to the tree:
         - If the connection does  not succeed, repeat from step  it:extend, up
        to   nb_trials=1000 times.
         - If the connection succeeds, add   x_end to   graph (with the correct
        backpointer), and then use Graph.path to return the path from   x_start
        to   x_end.
        """
        pass  # Substitute with your code
        return {}x_path{}
    
def rrt_search_test():
    """
    
     - Loads the variables   world,   x_start and   x_end from the file
    !70!DarkSeaGreen2 sphereWorld.mat.
     - For each starting location (column) in   x_start, and each goal
    location (column) in   x_goal, calls Rrt.search to find a path.
     - Calls Sphereworld.plot and then overimposes all the trajectories from
    the start locations to the goal location.
    """
    pass  # Substitute with your code
    

