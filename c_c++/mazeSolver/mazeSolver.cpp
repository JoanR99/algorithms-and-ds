#include "iostream"
#include "vector"

using namespace std;

class Point
{
public:
    int x, y;
};

bool walk(vector<string> maze, char wall, Point current, Point end, vector<vector<bool>> &seen, vector<Point> &path)
{
    vector<vector<int>> dir = {
        {0, -1},
        {1, 0},
        {0, 1},
        {-1, 0},
    };
    cout << "hola" << endl;
    // Base cases
    // 1. Off the map
    if (current.x < 0 || current.x >= sizeof(maze[0]) / sizeof(maze[0][0]) || current.y < 0 || current.y >= sizeof(maze[0]) / sizeof(maze))
    {
        return false;
    }

    // 2. On a wall
    if (maze[current.y][current.x] == wall)
    {
        return false;
    }

    // 3. End
    if (current.x == end.x && current.y == end.y)
    {
        path.push_back(current);
        return true;
    }

    // 4. Seen
    if (seen[current.x][current.y])
    {
        return false;
    }

    // Recursive cases
    //  Pre
    seen[current.x][current.y] = true;
    path.push_back(current);

    // Recurse
    for (int i = 0; i < dir.size(); i++)
    {
        vector<int> points = dir[i];
        Point point;
        point.x = points[0];
        point.y = points[1];

        if (walk(maze, wall, point, end, seen, path))
        {
            return true;
        }
    }

    // Post
    path.pop_back();
    return false;
};

vector<Point> solve(vector<string> maze, char wall, Point start, Point end)
{
    vector<bool> x(maze[0].size());
    vector<vector<bool>> seen(maze.size(), x);
    vector<Point> path;

    for (int i = 0; i < seen.size(); i++)
    {
        for (int j = 0; j < seen[0].size(); j++)
        {
            cout << seen[i][j] << endl;
        }
    }

    walk(maze, wall, start, end, seen, path);

    return path;
};

int main()
{
    vector<Point> result;
    vector<string> maze = {
        "### ",
        "# # ",
        "# # ",
        "    ",
        "# ##",
        "#   ",
        "# ##",
    };
    Point start;
    Point end;
    start.x = 1;
    start.y = 6;
    end.x = 3;
    end.y = 0;

    result = solve(maze, '#', start, end);

    cout << result.size() << endl;

    for (int i = 0; i < result.size(); i++)
    {
        cout << "result [" << i << "]: "
             << "y: " << result[i].y << " x: " << result[i].x << endl;
    }

    return 0;
}