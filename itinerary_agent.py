from mediatool.message_bus_mock import MessageBus
from planners.optimizer import optimize_candidates

class ItineraryAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus

    def handle_intent(self, intent):
        self.bus.publish('intent.requests', intent)
        responses = self.bus.collect_responses(intent['request_id'])
        candidates = [{'cost': 1000, 'comfort': 0.8}, {'cost': 800, 'comfort': 0.6}]
        best = optimize_candidates(candidates, weights=intent.get('weights', {'cost':0.5, 'comfort':0.5}))
        return best
