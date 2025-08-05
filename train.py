import argparse
from snake_rl.agent import train

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train the Snake RL agent')
    parser.add_argument('--episodes', type=int, help='Number of episodes to train (default: endless)')
    args = parser.parse_args()
    train(episodes=args.episodes)
