{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "ConnectionError",
     "evalue": "HTTPConnectionPool(host='0.0.0.0', port=9000): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x000000000612F780>: Failed to establish a new connection: [Errno 10049] The requested address is not valid in its context',))",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mConnectionError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-8ca0d1d23aa4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      6\u001b[0m }\n\u001b[1;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m \u001b[0mresp\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpost\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mC:\\Program Files\\Anaconda2\\lib\\site-packages\\requests\\api.pyc\u001b[0m in \u001b[0;36mpost\u001b[0;34m(url, data, json, **kwargs)\u001b[0m\n\u001b[1;32m    108\u001b[0m     \"\"\"\n\u001b[1;32m    109\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m--> 110\u001b[0;31m     \u001b[1;32mreturn\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'post'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    111\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mC:\\Program Files\\Anaconda2\\lib\\site-packages\\requests\\api.pyc\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(method, url, **kwargs)\u001b[0m\n\u001b[1;32m     54\u001b[0m     \u001b[1;31m# cases, and look like a memory leak in others.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     55\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0msessions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSession\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m---> 56\u001b[0;31m         \u001b[1;32mreturn\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     57\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m     58\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mC:\\Program Files\\Anaconda2\\lib\\site-packages\\requests\\sessions.pyc\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[1;32m    473\u001b[0m         }\n\u001b[1;32m    474\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m--> 475\u001b[0;31m         \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    476\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m    477\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mC:\\Program Files\\Anaconda2\\lib\\site-packages\\requests\\sessions.pyc\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, **kwargs)\u001b[0m\n\u001b[1;32m    594\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m    595\u001b[0m         \u001b[1;31m# Send the request\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m--> 596\u001b[0;31m         \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0madapter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    597\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m    598\u001b[0m         \u001b[1;31m# Total elapsed time of the request (approximately)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mC:\\Program Files\\Anaconda2\\lib\\site-packages\\requests\\adapters.pyc\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[1;32m    485\u001b[0m                 \u001b[1;32mraise\u001b[0m \u001b[0mProxyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m    486\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m--> 487\u001b[0;31m             \u001b[1;32mraise\u001b[0m \u001b[0mConnectionError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    488\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m    489\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mClosedPoolError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mConnectionError\u001b[0m: HTTPConnectionPool(host='0.0.0.0', port=9000): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x000000000612F780>: Failed to establish a new connection: [Errno 10049] The requested address is not valid in its context',))"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"http://0.0.0.0:9000/\"\n",
    "data = {\n",
    "    \"text\": \"when is this election going to end?\"\n",
    "}\n",
    "\n",
    "resp= requests.post(url, data=data)\n",
    "resp.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
