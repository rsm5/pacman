# coding=utf-8
# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
	"""
		A reflex agent chooses an action at each choice point by examining
		its alternatives via a state evaluation function.

		The code below is provided as a guide.  You are welcome to change
		it in any way you see fit, so long as you don't touch our method
		headers.
	"""

	def getAction(self, gameState):
		"""
		You do not need to change this method, but you're welcome to.

		getAction chooses among the best options according to the evaluation function.

		Just like in the previous project, getAction takes a GameState and returns
		some Directions.X for some X in the set {North, South, West, East, Stop}
		"""
		# Collect legal moves and successor states
		legalMoves = gameState.getLegalActions()

		# Choose one of the best actions
		scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		"Add more of your code here if you want to"

		return legalMoves[chosenIndex]

	def evaluationFunction(self, currentGameState, action):
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()

		newGhostStates = successorGameState.getGhostStates()

		"*** YOUR CODE HERE ***"

        #Fonte: https://github.com/iamjagdeesh/Artificial-Intelligence-Pac-Man/blob/master/Project%202%20Multi-Agent%20Pacman/multiAgents.py
		#       Artificial Intelligence A Modern Approach, Global Edition (Stuart J. Russell, Peter Norvig) (z-lib.org) - página 69

        """
			function SIMPLE-REFLEX-AGENT(percept) returns an action
                persistent: rules, a set of condition–action rules

                state ← I NTERPRET-INPUT(percept)
                rule ← RULE-MATCH(state, rules)
                action ← rule.ACTION
                return action
		"""

        '''
			Figure 2.10 A simple reflex agent. It acts according to a rule whose condition matches the
            current state, as defined by the percept.
		'''


		closestGhostPosition = newGhostStates[0].configuration.pos

		newFoodPositions = newFood.asList()
		foodDistances = [manhattanDistance(newPos, foodPosition) for foodPosition in newFoodPositions]

		distancia = manhattanDistance(newPos, closestGhostPosition)
		tmp2 = []
		for i in range(len( closestGhostPosition)):
				tmp2.append(closestGhostPosition[i]*10e6)


		lista = []
		bestScore = 10e6

		if len(foodDistances)==0:
			bestScore= foodDistances
		else:
			if distancia<=2:

				for i in range(len(newFoodPositions)):
					di = manhattanDistance(tuple(tmp2), newFoodPositions[i])
					lista.append(di)
				var =  min(lista)
				bestScore  -= var
			else:
				var2=  min(foodDistances)
				bestScore -=  var2+ len(foodDistances)*100

		return bestScore


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
		#Fonte: https://github.com/iamjagdeesh/Artificial-Intelligence-Pac-Man/blob/master/Project%202%20Multi-Agent%20Pacman/multiAgents.py
		#       Artificial Intelligence A Modern Approach, Global Edition (Stuart J. Russell, Peter Norvig) (z-lib.org) - página 196

        """
			function MINIMAX-SEARCH (game, state) returns an action
				player ← game.TO-MOVE (state)
				value, move ← MAX-VALUE (game, state)
				return move

			function MAX-VALUE (game, state) returns a (utility, move) pair
				if game.IS-TERMINAL (state) then return game.UTILITY (state, player), null
				v, move ← −∞
				for each a in game.ACTIONS (state) do
					v2, a2 ← MIN-VALUE (game, game.RESULT (state, a))
					if v2 > v then
						v, move ← v2, a
				return v, move

			function MIN-VALUE (game, state) returns a (utility, move) pair
				if game.IS-TERMINAL (state) then return game.UTILITY (state, player), null
				v, move ← +∞
				for each a in game.ACTIONS (state) do
					v2, a2 ← MAX-VALUE (game, game.RESULT (state, a))
					if v2 < v then
						v, move ← v2, a
				return v, move
		"""

        '''
			Figure 6.3 An algorithm for calculating the optimal move using minimax—the move that
			leads to a terminal state with maximum utility, under the assumption that the opponent plays
			to minimize utility. The functions MAX-VALUE and MIN-VALUE go through the whole
			game tree, all the way to the leaves, to determine the backed-up value of a state and the move
			to get there.
		'''

        def minimax(agent, depth, gameState):

            is_terminated = gameState.isLose() or gameState.isWin() or (depth == self.depth)

            if is_terminated:  # return the utility in case the defined depth is reached or the game is won/lost.
                return self.evaluationFunction(gameState)
            if agent == 0:  # maximize for pacman

				# E SE TIVERMOS MAIS DE UM AGENTE?
                return max(minimax(1, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent))

            else:  # minize for ghosts

                nextAgent = agent + 1  # calculate the next agent and increase depth accordingly.
                if gameState.getNumAgents() == nextAgent:
                    nextAgent = 0
                if nextAgent == 0:
                   depth += 1
                return min(minimax(nextAgent, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent))

        """Performing maximize action for the root node i.e. pacman"""
        action = Directions.SOUTH
        maximum = float("-inf")
        for agentState in gameState.getLegalActions(0):
            utility = minimax(1, 0, gameState.generateSuccessor(0, agentState))

            if utility > maximum:
                maximum, action = utility, agentState

        return action

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()

		# Fonte: https://github.com/iamjagdeesh/Artificial-Intelligence-Pac-Man/blob/master/Project%202%20Multi-Agent%20Pacman/multiAgents.py
		#        http://ai.berkeley.edu/multiagent.html#Q2
		#        Artificial Intelligence A Modern Approach, Global Edition (Stuart J. Russell, Peter Norvig) (z-lib.org) - página 200

        '''
		function ALPHA-BETA-SEARCH (game, state) returns an action
			player ← game.TO-MOVE (state)
			value, move ← MAX-VALUE (game, state, −∞, +∞)
			return move

		function MAX-VALUE (game, state, α, β) returns a (utility, move) pair
			if game.IS-TERMINAL (state) then return game.UTILITY (state, player), null
			v ← −∞
			for each a in game.A CTIONS (state) do
				v2, a2 ← MIN-VALUE (game, game.RESULT (state, a), α, β)
				if v2 > v then
					v, move ← v2, a
					α ← MAX (α, v)
				if v ≥ β then return v, move
			return v, move

		function MIN-VALUE (game, state, α, β) returns a (utility, move) pair
			if game.IS-TERMINAL (state) then return game.UTILITY (state, player), null
			v ← +∞
			for each a in game.ACTIONS (state) do
				v2, a2 ← MAX-VALUE (game, game.RESULT (state, a), α, β)
				if v2 < v then
					v, move ← v2, a
					β ← MIN (β, v)
				if v ≤ α then return v, move
			return v, move
		'''


        '''
		Figure 6.7 The alpha–beta search algorithm. Notice that these functions are the same as the
		MINIMAX-SEARCH functions in Figure 6.3, except that we maintain bounds in the variables
		α and β, and use them to cut off search when a value is outside the bounds.
		'''

        def maximizer(agent, depth, game_state, alpha, beta):  # maximizer function
            v = float("-inf")
            for newState in game_state.getLegalActions(agent):
                v = max(v, alphabetaprune(1, depth, game_state.generateSuccessor(agent, newState), alpha, beta))
                if v > beta:
                    return v
                alpha = max(alpha, v)
            return v

        def minimizer(agent, depth, game_state, alpha, beta):  # minimizer function
            v = float("inf")

            next_agent = agent + 1  # calculate the next agent and increase depth accordingly.
            if game_state.getNumAgents() == next_agent:
                next_agent = 0
            if next_agent == 0:
                depth += 1

            for newState in game_state.getLegalActions(agent):
                v = min(v, alphabetaprune(next_agent, depth, game_state.generateSuccessor(agent, newState), alpha, beta))
                if v < alpha:
                    return v
                beta = min(beta, v)
            return v

        def alphabetaprune(agent, depth, game_state, alpha, beta):
            is_terminated = game_state.isLose() or game_state.isWin() or (depth == self.depth)
            if is_terminated:  # return the utility in case the defined depth is reached or the game is won/lost.
                return self.evaluationFunction(game_state)

            if agent == 0:  # maximize for pacman
                return maximizer(agent, depth, game_state, alpha, beta)
            else:  # minimize for ghosts
                return minimizer(agent, depth, game_state, alpha, beta)

        """Performing maximizer function to the root node i.e. pacman using alpha-beta pruning."""
        action = Directions.SOUTH
        score = float("-inf")
        alpha = float("-inf")
        beta = float("inf")
        for agentState in gameState.getLegalActions(0):
            ghostValue = alphabetaprune(1, 0, gameState.generateSuccessor(0, agentState), alpha, beta)
            if ghostValue > score:
                score = ghostValue
                action = agentState
            if score > beta:
                return score
            alpha = max(alpha, score)

        return action


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

