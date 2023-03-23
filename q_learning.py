from .. environment import Environment, Outcome
import numpy as np


def eps_greedy(rng, qs, epsilon):
    # this function makes an epsilon greedy decision
    if rng.uniform(0, 1) < epsilon:
        # - with probability p == epsilon, an action is
        # chosen uniformly at random
        #print('greedy epsilon==p',rng.choice(list(qs)))
        return rng.choice(list(qs))
        pass
    else:
        return max(qs, key=qs.get)
        # - with probability p == 1 - epsilon, the action
        #   having the currently largest q-value estimate is chosen


class QLearning():
    def train(self, env: Environment):
        ########################################
        # please leave untouched
        rng = np.random.RandomState(1234)
        alpha = 0.2
        epsilon = 0.3
        gamma = env.get_gamma()
        n_episodes = 10000
        ########################################

        ########################################
        # initialize the 'table'
        Q = dict()
        for s in range(env.get_n_states()):
            Q[s] = dict()
            for a in range(env.get_n_actions()):
                Q[s][a] = 0.
        ########################################
        # TODO #################################
        for episode in range(1, n_episodes + 1):
            state = env.reset()
            done = False
            if (episode+1)%100==0:
                print('Episode',episode)
            while not done:
                action = eps_greedy(rng,Q[state],epsilon)
                # print('Action',action)
                next_state, reward, done = env.step(action)
                # print('Next state',next_state)
                # print('Reward',reward)
                Q[state][action] = Q[state][action] + alpha*(reward + gamma*max(Q[next_state].values()) - Q[state][action])
                state = next_state
                if done:
                    print('DONE')
                    break
            # TODO, exercise 3, generate an episode
            # with an eps_greedy policy, and then
            # implement the q-learning update here

            # you interact with the environment
            # ONLY via the methods
            #      'state = env.reset()'
            # and
            #      'state, reward, done = env.step(action)'
            #
            # 'state = env.reset()' is used to
            # reset the environment at the start
            # of an episode
            #
            # 'state, reward, done = env.step(action)'
            # is used to tell the environment that your
            # agent has decided to do 'action'.
            # the environment will then tell you, in
            # which state you actually ended up in,
            # what the immediate reward was, and whether
            # or not the episode ended.
        ########################################

        ########################################
        # this computes a deterministic policy
        # from the Q value function
        # along the way, we compute V, the
        # state value function as well
        policy = dict()
        V = dict()
        print('Q table ',Q.items())
        for s, qs in Q.items():
            policy[s] = dict()
            V[s] = 0.
            best_a = None
            best_q = float('-Inf')
            for a, q in qs.items():
                if q > best_q:
                    best_q = q
                    best_a = a

            # how good is it to be in state 's'?
            # if we take the best action, we can expect to get 'best_q'
            # future reward. hence, being in state V[s] we can expect
            # the same amount of reward ...
            V[s] = best_q
            for a in qs.keys():
                if a == best_a:
                    policy[s][a] = 1.
                else:
                    policy[s][a] = 0.
        ########################################

        return Outcome(n_episodes, policy, V=V, Q=Q)
