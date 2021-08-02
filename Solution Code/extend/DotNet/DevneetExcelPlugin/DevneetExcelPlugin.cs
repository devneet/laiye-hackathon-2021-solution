using Microsoft.Office.Interop.Excel;

namespace DevneetExcelPlugin
{
    public interface Plugin_Interface
    {   
        int Add(int number1, int number2);

        string getRangeOfCells(string filePath, string sheetName);
    }

    public class Plugin_Implement : Plugin_Interface
    {   
        public int Add(int number1, int number2)
        {
            return number1 + number2;
        }

        public string getRangeOfCells(string filePath, string sheetName)
        {

            string result = "";

            // Intialize Excel Workbook Parameters

            Application application = new Microsoft.Office.Interop.Excel.Application();
            application.DisplayAlerts = false;
            Workbook workBook = application.Workbooks.Open(filePath);
            application.Visible = false;

            // Intialize Excel Sheet Parameters

            Sheets workSheets = workBook.Worksheets;
            Worksheet excelSheet = workSheets.get_Item(sheetName);

            // Get Range Of Cells

            Range uRange = (Range)excelSheet.UsedRange.CurrentRegion;
            result = uRange.get_Address(false, false, XlReferenceStyle.xlA1, System.Type.Missing, System.Type.Missing);


            // Close Excel File

            workBook.Close(true);

            return result;

        }

    }
}
