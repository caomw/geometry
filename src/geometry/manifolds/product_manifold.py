from . import DifferentiableManifold, contract, np


class ProductManifold(DifferentiableManifold):
    @contract(components='seq[>=2,N](DifferentiableManifold)',
              weights='None|array[N](>0)')
    def __init__(self, components, weights=None):
        dim = sum([m.dimension for m in components])
        DifferentiableManifold.__init__(self, dimension=dim)
        self.components = components
        if weights is None:
            weights = np.ones(len(components))
        self.weights = weights

    @contract(a='seq')
    def belongs(self, a):
        if not len(a) == len(self.components): # XXX: what should I throw?
            raise ValueError('I expect a sequence of length %d, not %d.' % 
                             (len(a), len(self.components)))
        for x, m in zip(a, self.components):
            m.belongs(x)
    
    def distance(self, a, b): 
        ''' Computes the geodesic distance between two points. '''
        raise ValueError('Not implemented') # FIXME: finish this
        distances = [m.distance_(x) for x, m in zip(a, self.components)]
        distances = np.array(distances)
        return (distances * self.weights).sum()
        
    def logmap(self, a, b): 
        ''' Computes the logarithmic map from base point *a* to target *b*. '''
        raise ValueError('Not implemented') # FIXME: finish this
    
    def expmap(self, a, v):
        raise ValueError('Not implemented') # FIXME: finish this
        
    def project_ts(self, base, v_ambient):
        raise ValueError('Not implemented') # FIXME: finish this
    
    def __repr__(self):
        return 'P(%s)' % "x".join([str(x) for x in self.components])

