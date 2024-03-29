struct Expression
{
    virtual double evaluate() const = 0;
    virtual ~Expression() {}
};

struct Number : Expression
{
    Number(double value)
        : value(value)
    {}
    double evaluate() const {return value;}

private:
    double value;
};

struct BinaryOperation : Expression
{
    /*
      ����� op ��� ���� �� 4 ��������: '+', '-', '*' ��� '/', ��������������� ���������,
      ������� ��� ����� �����������.
     */
    BinaryOperation(Expression const * left, char op, Expression const * right)
        : left(left), op(op), right(right)
    { }
    ~BinaryOperation() {
        delete left;
        delete right;
    }
    double evaluate() const {
        switch (op) {
            case '+':
                return left->evaluate() + right->evaluate();
                break;
            case '-':
                return left->evaluate() - right->evaluate();
                break;
            case '*':
                return left->evaluate() * right->evaluate();
                break;
            case '/':
                return left->evaluate() / right->evaluate();
                break;
        }
    }
private:
    Expression const * left;
    Expression const * right;
    char op;
};