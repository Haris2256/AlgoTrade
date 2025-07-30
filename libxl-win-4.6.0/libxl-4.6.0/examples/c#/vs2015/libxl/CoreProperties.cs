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
    public class CoreProperties
    {
        public IntPtr handle;        

        public CoreProperties(IntPtr handle)
        {
            this.handle = handle;            
        }

        public string title
        {
            get
            {                
                IntPtr pStr = xlCorePropertiesTitle(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetTitle(handle, value); }
        }

        public string subject
        {
            get
            {
                IntPtr pStr = xlCorePropertiesSubject(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetSubject(handle, value); }
        }

        public string creator
        {
            get
            {
                IntPtr pStr = xlCorePropertiesCreator(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetCreator(handle, value); }
        }

        public string lastModifiedBy
        {
            get
            {
                IntPtr pStr = xlCorePropertiesLastModifiedBy(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetLastModifiedBy(handle, value); }
        }

        public string created
        {
            get
            {
                IntPtr pStr = xlCorePropertiesCreated(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetCreated(handle, value); }
        }

        public double createdAsDouble
        {
            get { return xlCorePropertiesCreatedAsDouble(handle); }                
            set { xlCorePropertiesSetCreatedAsDouble(handle, value); }
        }

        public string modified
        {
            get
            {
                IntPtr pStr = xlCorePropertiesModified(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetModified(handle, value); }
        }

        public double modifiedAsDouble
        {
            get { return xlCorePropertiesModifiedAsDouble(handle); }
            set { xlCorePropertiesSetModifiedAsDouble(handle, value); }
        }

        public string tags
        {
            get
            {
                IntPtr pStr = xlCorePropertiesTags(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetTags(handle, value); }
        }

        public string categories
        {
            get
            {
                IntPtr pStr = xlCorePropertiesCategories(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetCategories(handle, value); }
        }

        public string comments
        {
            get
            {
                IntPtr pStr = xlCorePropertiesComments(handle);
                String s = Marshal.PtrToStringAuto(pStr);
                return s;
            }
            set { xlCorePropertiesSetComments(handle, value); }
        }

        public void removeAll()
        {
            xlCorePropertiesRemoveAll(handle);
        }

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesTitle(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetTitle(IntPtr handle, string title);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesSubject(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetSubject(IntPtr handle, string subject);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesCreator(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetCreator(IntPtr handle, string creator);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesLastModifiedBy(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetLastModifiedBy(IntPtr handle, string lastModifiedBy);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesCreated(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetCreated(IntPtr handle, string created);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern double xlCorePropertiesCreatedAsDouble(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetCreatedAsDouble(IntPtr handle, double created);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesModified(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetModified(IntPtr handle, string modified);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern double xlCorePropertiesModifiedAsDouble(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetModifiedAsDouble(IntPtr handle, double modified);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesTags(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetTags(IntPtr handle, string tags);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesCategories(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetCategories(IntPtr handle, string categories);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern IntPtr xlCorePropertiesComments(IntPtr handle);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesSetComments(IntPtr handle, string comments);

        [DllImport("libxl.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.Cdecl)]
        private static extern void xlCorePropertiesRemoveAll(IntPtr handle);
    }
}
