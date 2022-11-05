from optparse import *
from colorama import init
from Display import *
from Display import squencial
import threading
import datetime


init();
R = "\033[31m"
G = "\033[92m"
W = "\033[00m"

use = OptionParser("""{}
	                                    WWNNXXXKKKKKKKKKXXXNNWW
                                      WNXXK00OOOOOOOOO00OOOOOOOOO00KXNW
                                  WNXK0OOOO000KKKKXXXXXXXXXKKKK000OOOO00KNW
                               WNK0OkOO00KKXXNNNWWWWWWWWWWWWWNNNXXKK00OOkO0KNW
                             WX0OkO00KKXNNWWWWWWWWWWWWWWWWWWWWWWWWWNNXKK00Okk0KNW
                           NKOkkO0KKXNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXXK0OkkOKNW
                         WKOkkO0KXXNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXK0OkkkKN
                       WXOkkO0KXNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNXK0OkkkKW
                      WKkkkO0KXNNNNNNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNXK0OOkx0N
                     N0xkO0KXXNNNNNNNNNNNNNNNNWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNXXK0OkxOX
                    NOxkO0KXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXK0OkxkXW
                   NOxkOOKXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXK0OkxkX
                  W0xxkO0KXXXXXXXXNNNNNNKOkxkKXNNNNNNNNNNNNNNNNKOxxOKXNNNNNXXXXXXXXK0OkxxkN
                 WKxxkO0KKXXXXXXXXXXNNXkl:;;;cdKNNNNNNNNNNNNNKxc:;;;cxKNNXXXXXXXXXXKK0Okxx0W
                 NkdxkO0KKKKXXXXXXXXXKx::::::::o0NNNNNNNNNNNKd::::::::dKXXXXXXXXXXKKK0OkkdxX
                WKxxkOO0KKKKKKXXXXXXXOc:::ccc:::xXNXNNNNNNNXkc:::cc:::cxXXXXXXXKKKKKK0OOkxdOW
                WOdxkOO00KKKKKKKXXXXKx:cdk00Oxl:o0NXXXXXXXXKd:cdk00Odl:oKXXXXXKKKKKKK00OkxdkN
                NkdxkOO0000KKKKKKKXXKdlkKXXXXX0oo0XXXXXXXXXKdoOXXXXXXOoo0XXKKKKKKK0000OOkxdxX
                XxdxkkO000000KKKKKKKKOOXXXXXXXX0OKXXXXXXXXXKO0XXXXXXXX0OKKKKKKKKK00000OOkxddK
                XxdxxkOOO000000KKKKKKKKXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKK00000OOOkkxddK
                XxoxxkkOOOO00000KKKKKKKKKKKXXXXXXXXXKXXXKXXXXXXXXXXKKKKKKKKKK00000OOOOkkxxddK
                NkodxxkkkOOOOkkOO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK000OkkOOOOkkkxxdoxX
                W0ddxxxkkkkOx:;:cclodxkOO00KKKKKKKKKKKKKKKKKKKKKKK00OOkxdolcc:;:dOkkkkxxxdokN
                 Xxodxxxkkkkd;;odoolccccccclloodddxxxxxxxxxdddoolllccccccllodd:;okkkkxxxdodKW
                 WOoodxxxkkkkl;o0KKKKK00OOkkxddoooolllllllloooddxxkkO000KKKK0x;cxkkkxxxdookN
                  Nkoodxxxxkkxc:x0KXXXNNNNWWWWWWNNNNNNNNNNNNNNWWWWNNNNNXXXKKkc:dkkxxxxddodK
                   Xxooddxxxkkd::ldxkO0KXNNWWWWWWWWWWWWWWWWWWWWWWNNNXK00Oxdo::okkxxxdddoo0W
                   WKdloddxxxxkdc,,;;:clloddxkkOO0000K000000OOkkxxdoolc::;,,:dxxxxxddolo0W
                    WKdlodddxxxkxl:;;::::::::::::::::cccc:::::::::::::::;;;ldxxxxdddolo0W
                     WXkolodddxxxxdl:;:::::::::::::::::::::::::::::::::;:coxxxxdddooldKW
                       NOdloodddxxxxdl:;;:::::::::ccccccccccc::::::::;:coxxxddddoolokNW
                        WXkolooddddxxxdoc::::::::::::cccc:::::::::::cldxxxddddoollxKW
                          WKkoloodddddxxxdollc:::::::::::::::::cclodxxxdddddoolox0N
                            WXkdlloodddddxxxxxddoollllllllloooddxxxxdddddoollokKW
                              WN0kdllooodddddddxxxxxxxxxxxxxxxdddddddooollox0XW
                                 WN0kxolloooodddddddddddddddddddoooollodk0XW
                                     WX0OkdoolloooooooooooooollloodxO0XNW
                                         WWXKK0OkkxxxxxxxxxkkOO0KXNW
                                                  WWWWWWWWW

--------------------------------------------------------------------------------------------------------------                                             
--------------------------------------------------------------------------------------------------------------
-m --mode\t\t\t Display/VideoGame

                                                  {}""".format(R,G));

use.add_option("-m", "--mode", dest="mode", help="display/videoGame");
(values, args) = use.parse_args();

#value = values.mode.lower();

if values.mode == "display":
	sqal =  squencial.Squencial(1200,750);
	sqal.modelD();
elif values.mode == "videogame":
	sqal =  squencial.Squencial(400,250);
	thding1 = threading.Thread(target=sqal.modelD);
	thding1.start();
else:
	print(use.usage);





