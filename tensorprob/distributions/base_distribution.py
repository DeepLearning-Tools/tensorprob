import tensorflow as tf

from .. import config
from .. import utilities


class BaseDistribution(tf.Tensor):
    def __init__(self, name=None):
        from ..model import Model

        Model.current_model.track_variable(self)

        # Get the op of a new placeholder and use it as our op
        placeholder = tf.placeholder(dtype=config.dtype, name=name or utilities.generate_name())
        my_op = placeholder.op
        # .clear() doesn't exist in Python 2:
        del my_op.outputs[:]
        my_op.outputs.append(self)

        super(BaseDistribution, self).__init__(my_op, 0, config.dtype)

    def logp(self):
        raise NotImplementedError

    def pdf(self):
        raise NotImplementedError

    def cdf(self, lim):
        raise NotImplementedError
