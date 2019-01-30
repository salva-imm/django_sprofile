
from __future__ import with_statement

import pstats
from django.conf import settings
try:
    import cProfile 
except ImportError:
    import profile
    
# import StringIO
from io import StringIO



class sProfilerMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response

    def can(self, request):
        if settings.DEBUG and settings.PROFILER["enable"]:
            return True

           
    def __call__(self, request):
        if self.can(request):
            self.profiler = cProfile.Profile()
            self.profiler.enable()
            response = self.get_response(request)
            self.profiler.disable()
            s = StringIO()
            
            sortby = settings.PROFILER.get('sort', 'time')  
            count = settings.PROFILER.get('count', None)
            output = settings.PROFILER.get('output', ['console'])
            
            ps = pstats.Stats(self.profiler, stream=s).sort_stats(sortby).print_stats(count)

            for output in settings.PROFILER.get('output', ['console','file']):
                
                if output == 'console':
                    print(s.getvalue())

                if output == 'file':
                    file_loc = settings.PROFILER.get('file_location', 'profiling_results.txt')
                    with open(file_loc,'a+') as file:
                        counter = str(s.getvalue())
                        file.write(counter)

        return response

       
