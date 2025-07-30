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

using System;
using System.Runtime.InteropServices;

namespace libxl
{
    public class Table
    {
        public IntPtr handle;
        Book book;

        public Table(IntPtr handle, Book book)
        {
            this.handle = handle;
            this.book = book;
        }

        public string name
        {
            get
            {
                IntPtr pStr = xlTableName(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set
            {
                xlTableSetName(handle, value);
            }
        }

        public string reference
        {
            get
            {
                IntPtr pStr = xlTableRef(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set
            {
                xlTableSetRef(handle, value);
            }
        }

        public AutoFilter autoFilter()
        {
            IntPtr autoFilterHandle = xlTableAutoFilter(handle);
            return new AutoFilter(autoFilterHandle, book);
        }

        public TableStyle tableStyle
        {
            get { return (TableStyle)xlTableStyle(handle); }
            set { xlTableSetStyle(handle, (int)value); }
        }

        public bool showRowStripes
        {
            get { return xlTableShowRowStripes(handle) > 0; }
            set { xlTableSetShowRowStripes(handle, value ? 1 : 0); }
        }

        public bool showColumnStripes
        {
            get { return xlTableShowColumnStripes(handle) > 0; }
            set { xlTableSetShowColumnStripes(handle, value ? 1 : 0); }
        }

        public bool showFirstColumn
        {
            get { return xlTableShowFirstColumn(handle) > 0; }
            set { xlTableSetShowFirstColumn(handle, value ? 1 : 0); }
        }

        public bool showLastColumn
        {
            get { return xlTableShowLastColumn(handle) > 0; }
            set { xlTableSetShowLastColumn(handle, value ? 1 : 0); }
        }

        public int columnSize()
        {
            return xlTableColumnSize(handle);
        }

        public string columnName(int columnIndex)
        {
            IntPtr pStr = xlTableColumnName(handle, columnIndex);
            String s = Marshal.PtrToStringAuto(pStr);
            return s;
        }

        public bool setColumnName(int columnIndex, string name)
        {
            return xlTableSetColumnName(handle, columnIndex, name);
        }
        
        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlTableName(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetName(IntPtr handle, string name);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlTableRef(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetRef(IntPtr handle, string reference);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlTableAutoFilter(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern int xlTableStyle(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetStyle(IntPtr handle, int tableStyle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern int xlTableShowRowStripes(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetShowRowStripes(IntPtr handle, int showRowStripes);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern int xlTableShowColumnStripes(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetShowColumnStripes(IntPtr handle, int showColumnStripes);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern int xlTableShowFirstColumn(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetShowFirstColumn(IntPtr handle, int showFirstColumn);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern int xlTableShowLastColumn(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlTableSetShowLastColumn(IntPtr handle, int showLastColumn);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern int xlTableColumnSize(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlTableColumnName(IntPtr handle, int columnIndex);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern bool xlTableSetColumnName(IntPtr handle, int columnIndex, string name);
    }
}

