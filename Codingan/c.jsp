<%-- 
    Document   : view
    Created on : 8 Dec 2024, 22.06.09
    Author     : ASUS
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
    <title>View Data Barang</title>
</head>
<body>
    <h1>Data Barang</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nama Barang</th>
            <th>Jumlah</th>
            <th>Harga</th>
            <th>Action</th>
        </tr>
        <%
            Connection conn = null;
            Statement stmt = null;
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db_barang", "root", "");
                stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery("SELECT * FROM barang");

                while (rs.next()) {
                    out.println("<tr>");
                    out.println("<td>" + rs.getInt("id") + "</td>");
                    out.println("<td>" + rs.getString("nama_barang") + "</td>");
                    out.println("<td>" + rs.getInt("jumlah") + "</td>");
                    out.println("<td>" + rs.getDouble("harga") + "</td>");
                    out.println("<td><a href='edit.jsp?id=" + rs.getInt("id") + "'>Edit</a></td>");
                    out.println("</tr>");
                }
            } catch (Exception e) {
                e.printStackTrace(out);
            } finally {
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            }
        %>
    </table>
    <br>
    <a href="add.jsp">Tambah Data</a>
</body>
</html>

