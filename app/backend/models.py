from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Result(Base):
    __tablename__ = 'results'
    id: Mapped[int] = mapped_column(primary_key=True)
    expression: Mapped[str] = mapped_column()
    result: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"<Result(id={self.id}, expression={self.expression}, result={self.result})>"