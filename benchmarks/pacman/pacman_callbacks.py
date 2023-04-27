from src.wrappers.shield_callbacks import ShieldingCallback


class PacmanShieldingCallback(ShieldingCallback):

    def _on_step(self):
        for idx, env in enumerate(self.locals["env"].envs):
            #self.logger.record('stats/full', env.full)
            #self.logger.record('stats/empty', env.empty)
            #self.logger.record('stats/switch_violations', env.switch_violations)
            #self.logger.record('stats/episodes', env.episodes_count)
            #self.logger.record('stats/successful_episodes', env.successful_episodes)
            self.logger.record('stats/penalty', env.penalty)
            self.logger.record('stats/die', env.die)
            self.logger.record('stats/max_score', env.max_score)
            self.logger.record('stats/score', env.score)
        return super(PacmanShieldingCallback, self)._on_step()