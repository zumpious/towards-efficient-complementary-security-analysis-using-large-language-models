exemplary_prompt = """
  Analyze the following potential vulnerability that was found by the security scanner "SpotBugs" with the "FindSecurityBugs"-Plugin in a Java source code project.
  Vulnerability identified by the security scanner and contextual information:
  Source code: ```/**
    * OWASP Benchmark Project v1.2
    *
    * <p>This file is part of the Open Web Application Security Project (OWASP) Benchmark Project. For
    * details, please see <a
    * href="https://owasp.org/www-project-benchmark/">https://owasp.org/www-project-benchmark/</a>.
    *
    * <p>The OWASP Benchmark is free software: you can redistribute it and/or modify it under the terms
    * of the GNU General Public License as published by the Free Software Foundation, version 2.
    *
    * <p>The OWASP Benchmark is distributed in the hope that it will be useful, but WITHOUT ANY
    * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
    * PURPOSE. See the GNU General Public License for more details.
    *
    * @author Dave Wichers
    * @created 2015
    */
  package org.owasp.benchmark.testcode;
  import java.io.IOException;
  import javax.servlet.ServletException;
  import javax.servlet.annotation.WebServlet;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;
  @WebServlet(value = "/sqli-03/BenchmarkTest01620")
  public class BenchmarkTest01620 extends HttpServlet {
      private static final long serialVersionUID = 1L;
      @Override
      public void doGet(HttpServletRequest request, HttpServletResponse response)
              throws ServletException, IOException {
          doPost(request, response);
      }
      @Override
      public void doPost(HttpServletRequest request, HttpServletResponse response)
              throws ServletException, IOException {
          response.setContentType("text/html;charset=UTF-8");
          String[] values = request.getParameterValues("BenchmarkTest01620");
          String param;
          if (values != null && values.length > 0) param = values[0];
          else param = "";
          String bar = new Test().doSomething(request, param);
          String sql = "{call " + bar + "}";
          try {
              java.sql.Connection connection =
                      org.owasp.benchmark.helpers.DatabaseHelper.getSqlConnection();
              java.sql.CallableStatement statement = connection.prepareCall(sql);
              java.sql.ResultSet rs = statement.executeQuery();
              org.owasp.benchmark.helpers.DatabaseHelper.printResults(rs, sql, response);
          } catch (java.sql.SQLException e) {
              if (org.owasp.benchmark.helpers.DatabaseHelper.hideSQLErrors) {
                  response.getWriter().println("Error processing request.");
                  return;
              } else throw new ServletException(e);
          }
      } // end doPost
      private class Test {
          public String doSomething(HttpServletRequest request, String param)
                  throws ServletException, IOException {
              String bar;
              String guess = "ABC";
              char switchTarget = guess.charAt(2);
              // Simple case statement that assigns param to bar on conditions 'A', 'C', or 'D'
              switch (switchTarget) {
                  case 'A':
                      bar = param;
                      break;
                  case 'B':
                      bar = "bobs_your_uncle";
                      break;
                  case 'C':
                  case 'D':
                      bar = param;
                      break;
                  default:
                      bar = "bobs_your_uncle";
                      break;
              }
              return bar;
          }
      } // end innerclass Test
  } // end DataflowThruInnerClass
  ```
  CWE ID: 89
  Category: sqli
  Type of potential vulnerability: SQL_INJECTION_JDBC
  Method: doPost
  Line of code: 50
  The source code included might be a false positive classification by the SAST scanner.
  Do you agree with the scanner that this source code contains an actual vulnerability?
  Return a number for your decision ranging from "0.0" to "10.0", where "10.0" means you absolutely agree with the scanner, "0.0" means you absolutely do not agree, and any number around "5.0" means that you are not sure.
  Think step by step. 
  Give your answer in the following format:
  ```
  Explanation: "Let\'s think step by step..." 
  ---
  Decision: 0.0 - 10.0
  ```
  Explanation:
"""
