using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
        // UpdatePosition uses player input to update the x and y coordinates
        public new static void UpdatePosition(string key, out int x, out int y)
        {
            switch (key)
            {
                case "LeftArrow":
                    x = -1;
                    y = 0;
                    break;
                case "RightArrow":
                    x = 1;
                    y = 0;
                    break;
                case "UpArrow":
                    x = 0;
                    y = -1;
                    break;
                case "DownArrow":
                    x = 0;
                    y = 1;
                    break;
                default:
                    x = 1;
                    y = 0;
                    break;
            }
        }
        // UpdateCursor uses the player input to update what the player looks like on screen aka which way the player is facing
        public new static char UpdateCursor(string key)
        {
            char Player;
            switch (key)
            {
                case "LeftArrow":
                    Player = '<';
                    break;
                case "RightArrow":
                    Player = '>';
                    break;
                case "UpArrow":
                    Player = '^';
                    break;
                case "DownArrow":
                    Player = 'v';
                    break;
                default:
                    Player = '<';
                    break;
            }
            return Player;
        }
        // KeepInBounds is insuring the player stays between 0 and the max value of the x and y axis since 0:0 is top left
        public new static int KeepInBounds(int current_coordinate, int max_screen_value)
        {
            return current_coordinate < 0 ? 0 : current_coordinate >= max_screen_value ? max_screen_value - 1 : current_coordinate;
        }
        // DidScore returns true if the player is at the x y of the fruit
        public new static bool DidScore(int x_char, int x_fruit, int y_char, int y_fruit)
        {
            return x_char == x_fruit && y_char == y_fruit;
        }
    }
}