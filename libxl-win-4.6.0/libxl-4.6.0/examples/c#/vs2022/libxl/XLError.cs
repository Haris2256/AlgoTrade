///////////////////////////////////////////////////////////////////////////////
//                                                                           //
//                   LibXL .NET wrapper version 4.6.0                        //
//                                                                           //
//                 Copyright (c) 2008 - 2025 XLware s.r.o.                   //
//                                                                           //
//   THIS FILE AND THE SOFTWARE CONTAINED HEREIN IS PROVIDED 'AS IS' AND     //
//                COMES WITH NO WARRANTIES OF ANY KIND.                      //
//                                                                           //
///////////////////////////////////////////////////////////////////////////////

namespace libxl
{
    public class XLError : System.Exception
    {
        public XLError(string message)
            : base("libxl: " + message)
        {
        }
    }
}
